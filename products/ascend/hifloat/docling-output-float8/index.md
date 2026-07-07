## Ascend HiFloat8 Format for Deep Learning

Yuanyong Luo ∗ , Zhongxing Zhang, Richard Wu, Hu Liu, Ying Jin

HiSilicon, Huawei Kai Zheng, Minmin Wang, Zhanying He Central Hardware, Huawei

Guipeng Hu, Luyao Chen, Tianchi Hu, Junsong Wang Computing Product Line, Huawei

Minqi Chen, Mikhaylov Dmitry, Korviakov Vladimir, Bobrin Maxim, Yuhao Hu, Guanfu Chen, Zeyi Huang

Central Media, Huawei

## Abstract

This preliminary white paper proposes a novel 8-bit floating-point data format HiFloat8 (abbreviated as HiF8) for deep learning. HiF8 features tapered precision. For normal value encoding, it provides 7 exponent values with 3-bit mantissa, 8 exponent values with 2-bit mantissa, and 16 exponent values with 1-bit mantissa. For denormal value encoding, it extends the dynamic range by 7 extra powers of 2, from 31 to 38 binades (notice that FP16 covers 40 binades). Meanwhile, HiF8 encodes all the special values except that positive zero and negative zero are represented by only one bit-pattern. Thanks to the better balance between precision and dynamic range, HiF8 can be simultaneously used in both forward and backward passes of AI training. In this paper, we will describe the definition and rounding methods of HiF8, as well as the tentative training and inference solutions. To demonstrate the efficacy of HiF8, massive simulation results on various neural networks, including traditional neural networks and large language models (LLMs), will also be presented.

## 1 Introduction

In 2020, several of our top chip architects foresaw that as Moore's Law [1] slows down, low-precision training and inference would be an important way to reduce the computing power and mitigate the memory wall [2] for AI hardware. Thus in 2021, HiSilicon launched the HiFloat project, aiming to study and develop novel low-precision data formats for our AI products. Subsequently, this project attracted many researchers from other departments to join. In this paper, we will officially disclose some of our research achievements on Float8.

First, let's take a brief look at history. Generally, the development of AI data formats can be divided into the following four phases based on the time for commercial use:

Phase 1 (1959 - 2006): FP64. The concept of AI was first proposed in 1956. Then, several theoretical prototypes and directions were established and developed, including backpropagation algorithm [3], convolutional neural network (CNN) [4], and long short-term memory [5]. During this period, CPUs were the major AI hardware, and the mainstream data format was the 64-bit double precision floating-point format FP64 defined in IEEE Standard for Floating-Point Arithmetic [6] in 1985. Prior to this, some predecessors of FP64 were in use.

Phase 2 (2006 - now): FP32. In 2006, FP32 was used for the first time to train CNNs on GPUs and achieved a four-fold performance improvement compared with FP64 training on CPUs [7]. The bit width of FP32 is only half that of FP64. Therefore, a chip that uses the FP32 format can store more data and integrate more multiply-accumulate (MAC) units than one that uses FP64. The single instruction, multiple data (SIMD) computing mode enables GPUs to have a significantly higher degree of computing parallelism than CPUs [8]. Finally, AlexNet [9] which ran on two GPUs won the championship of ILSVRC 2012, making FP32 the mainstream data format for deep learning training from 2012 to 2017.

Phase 3 (2017 - now): Float16 mixed precision. In 2016, Google proposed a novel Float16 data format in its TensorFlow white paper [10]. This format was equivalent to FP32 without the last 16 bits and was used as the input data format of multiplication, whereas FP32 was used for accumulation in the general matrix-matrix multiplication (GEMM). This format was later named Brain Floating Point 16 (BF16) [11] and deployed on Tensor Processing Unit (TPU) [12] V2 and V3 . In 2017, Google's AlphaGo [13] powered by TPU V2 defeated the world's number one Go player Ke Jie in all three games, causing a global sensation. Unlike Google, NVIDIA and Huawei adopt the IEEE 754 half-precision data format [14]. NVIDIA released the V100 GPU [15] in 2017 and Huawei shipped the Ascend NPU [16] in 2019. Both the GPU and NPU support the FP16 and FP32 mixed precision training strategy, with backward global loss-scaling to prevent excessive zero-valued activation gradients caused by narrow dynamic range of FP16 [17]. Since 2017, the Float16 mixed precision training solution, mainly consisting of BF16 and FP16, has become the main choices for deep learning. However, FP32 is still used for some networks that require high precision.

∗ Corresponding Author: luoyuanyong@{hisilicon.com, yeah.net}

Phase 4 (2022 - now): Float8 mixed precision. In 2018, IBM radically cut off the last 8 bits of FP16 to obtain a Float8 data format with 1 sign bit, 5 exponent bits, and 2 mantissa bits (E5M2) [18]. However, on MobileNetV2 and Transformer networks, the accuracy of E5M2 training decreased dramatically. Then in 2019, IBM further proposed the 8-bit hybrid FP8 (HFP8) training solution, with E4M3 (a Float8 format that has 1 sign bit, 4 exponent bits, and 3 mantissa bits) as the weights and activations format and E5M2 as the activation gradients format [19]. Thus, when calculating gradients in the backward pass, GEMM that supports mixed Float8 inputs is needed, and HFP8 is therefore called FP9 in hardware implementation [20]. In 2022, NVIDIA deployed HFP8 (renamed as FP8) mixed precision solution with twice the computing power of FP16 on its new H100 GPU, and shipped by the end of the year [21]. Subsequently, Intel, ARM, AMD, and Quanlcomm et al., announced that they would also support this solution [22, 23].

From a brief historical review, we can see that low-precision training [24] has always been an important direction to improve AI performance. And the commercial use of Float8 mixed precision has begun. However, it is also important to note that the trade-off between precision and dynamic range is challenging in the evolution from Float16 to Float8. For Float16, one fixed field-width format (either BF16 or FP16), could be elegant to cover all GEMM inputs, and works well for almost all scenarios. But this failed in Float8 mixed precision. In addtion to the research for fixed field-width formats, Posit [25] is a decent exploration for tapered precision data type, because it matches the centralized characteristic of AI data distribution during training and inference. Unfortunately, Posit16 failed in the competition for Float16 mixed precision, due to its larger hardware cost than BF16 and FP16, and insignificant precision improvement for training [26]. And Posit8 also failed in the competition for Float8 mixed precision, because its encoding method cannot balance the precision and dynamic range very well to meet the training requirement [27,28].

Inspired by FP16, Posit, and HFP8/FP8, this paper proposes a novel 8-bit floating point format HiF8 for deep learning, which features the better balance between precision and dynamic range compared with the existing Float8 formats, and can be simultaneously used in both forward and backward passes for AI training. A large number of simulation results would be presented to illustrate the advantages of HiF8 in this paper.

## 2 HiFloat8

This section first describes the definition of the novel 8-bit floating-point data format HiF8, including the support for special values. Then, some consideration and design issues for HiF8 will be explained.

## 2.1 Novel Data Format

We propose a new general-purpose floating-point enconding and decoding method for data expression, for which the field width, dynamic range, and significand precision can be scaled based on scenario requirements. This paper focuses on the 8-bit floating-point instance for deep learning usage. On the basis of the IEEE 754 [14], HiF8 defines an additional dot field . Therefore, HiF8 consists of the four fields as listed in Table 1: a sign field, a dot field, an exponent field, and a mantissa field.

Table 1: Fields of HiF8

|               | Sign    | Dot: D                        | Exponent: E                              | Mantissa                             |
|---------------|---------|-------------------------------|------------------------------------------|--------------------------------------|
| Width: Values | 1 1 1 1 | 2: {2, 3, 4} 3: 1 4: 0 4: DML | D: ± [2 , 15] D: ± 1 D: 0 -Denormal Sign | 5 - D = [1, 3] 4 - D = 3 3 - D = 3 3 |

The following describes each field in detail:

- Sign Filed: 1 bit , determining the sign of the HiF8 number, which is the sign of the significand as well. By default, 1 indicates the negative sign and 0 indicates the positive sign.
- Dot Field: 2 to 4 bits , used to code the five D values (0 to 4) and the sign of DenorMaL (DML). D value explicitly indicates the number of bits occupied by the exponent field, and implies the number of bits occupied by the mantissa field. DML sign specifies that the HiF8 number has no exponent field, and needs to be parsed by denormal equation (2). Otherwise, NorMaL (NML) equation (1) should be used. The dot field is coded using unconventional prefix codes, that is, the 4-bit width is used for coding small value 0 and DML sign, the 3-bit width is used for coding medium value 1, whereas the 2-bit width is used for coding large values 2, 3, and 4. Table 2 specifies the default mapping, in which values with a 2 in the subscript are binary, otherwise they are decimal.
- Exponent Field: D bits (an implicit leading magnitude bit with value 1 unstored), where D is equal to the coded value of the dot field and D ∈ { 0 , 1 , 2 , 3 , 4 } . Different from the offset-binary method used in the IEEE 754, the exponent field

Table 2: Unconventional Prefix Code for Dot Field

| Width      | 2      |        |        | 3       | 4        |            |
|------------|--------|--------|--------|---------|----------|------------|
| Code Value | 11 2 4 | 10 2 3 | 01 2 2 | 001 2 1 | 0001 2 0 | 0000 2 DML |

of HiF8 uses sign-magnitude code to represent values. But the most significant bit (MSB) of the magnitude is fixed to 1. Mark the sign of exponent as Se. By default, 1 means negative sign and 0 means positive sign. Then denote the complete sign-maginitude exponent as Ei in binary mode, we have:

<!-- formula-not-decoded -->

Since the fixed MSB of the magnitude can be hidden, Ei is simplified as Em in the memory format:

<!-- formula-not-decoded -->

The number of bits in Em equals the value of D. When D is zero, Em dose not occupy any bit width, indicating that the exponent value equals zero.

- Mantissa Field: 1 to 3 bits (an implicit leading significand bit with value 1 unstored), coded by unsigned integer. For the normal number of HiF8, mantissa represents the fractional bits (to the right of the binary point) in the significand. For the denormal value of HiF8, mantissa represents the extended exponents in a biased form.

So far, we have introduced the four fields for HiF8. Table 3 summarizes the corresponding code-value mapping details. In the memory format, dot field is stored as outlined in Table 2. Exponent field is stored as Em with an implicit bit. Em can be further interpreted as Ei in binary mode, and E in decimal mode.

Table 3: HiF8 Code-Value Mapping Details

| Value of Dot                                       | DML           | 0          | 1            | 2                                    | 3                                        | 4                                         |
|----------------------------------------------------|---------------|------------|--------------|--------------------------------------|------------------------------------------|-------------------------------------------|
| Em (binary) Ei (binary) E (decimal) Mantissa Width | N/A N/A N/A 3 | None 0 0 3 | Se Se, ± 1 3 | Se, Mag[2] Se, 1, Mag[2] ± [2 , 3] 3 | Se, Mag[2:3] Se, 1, Mag[2:3] ± [4 , 7] 2 | Se, Mag[2:4] Se, 1, Mag[2:4] ± [8 , 15] 1 |

Denote the sign as S, and the mantissa as M. For the normal number, HiF8 should be interpreted as:

<!-- formula-not-decoded -->

In the normal equation (1), 2 bit-patterns with the largest absolute value ( 2 15 × 1 . 5 ) should be interpreted specially for Infinities . For the denormal number, HiF8 should be interpreted as:

<!-- formula-not-decoded -->

In the denormal equation (2), M ∈ [1 , 7] , which offers 7 addtional exponent values of [-22, -16]. 2 bit-patterns with M = 0 should be interpreted specially for Zero and NaN (Not a Number).

Table 4: Typical Values and Features for HiF8, FP8 and FP16

|                                                                                                                  | FP16                                                                                                | HiF8                                                                                                                                | FP8-E4M3                                                                    | FP8-E5M2                                                                               |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| Infinities NaN Zero Max Positive NML Min Positive NML Max Positive DML Min Positive DML Exponent Exponent (+DML) | Support Support Support 2 15 × (2 - 2 - 10 ) 2 - 14 2 - 14 × (1 - 2 - 10 2 - 24 [-14, 15] [-24, 15] | S 1101111 2 10000000 2 00000000 2 01101110 2 = 2 15 01111110 2 = 2 - 15 00000111 2 = 2 - 16 00000001 2 = 2 - 22 [-15, 15] [-22, 15] | N/A Support Support 1 . 75 × 2 8 2 - 6 1 . 75 × 2 - 7 2 - 9 [-6, 8] [-9, 8] | Support Support Support 1 . 75 × 2 15 2 - 14 1 . 5 × 2 - 16 2 - 16 [-14, 15] [-16, 15] |

Table 4 shows some typical encoding values and features for HiF8, FP8 [22] and FP16 [14] formats. For the HiF8 format in binary mode, the black bit is the sign field, the red bits are the dot field, the green bits are exponent field, and the blue bits are the mantissa field. Obviously, HiF8 supports all special values, but does not distinguish between positive zero and negative zero because it's not necessary for deep learning. In addition to the regular exponent range, Table 4 also lists the exponent range after denormal to normal operation, which is critical to measuring the dynamic range of a floating point format. To clearly illustrate the differences between HiF8 and FP8, Fig. 1 further plots the distribution of significand bits on the exponent after denormal to normal operation.

Figure 1: Significand Precision over Exponent

![图1](images/page_000.png)

## 2.2 Consideration and Design

Before the launch of the HiFloat project, we investigated lots of literatures on low-percision training. Finally, three data formats were selected as the references. The first is the FP16 defined by the IEEE 754 [14], with the global backward loss-scaling method [29], this data type trains well for almost all neural networks. The second is the HFP8 [19] proposed by IBM, which is the first 8-bit floating point format for commercial use [21]. The third is the Posit [25] invented by John Gustafson, which features the tapered precision that matches the centralized characteristic of AI data distribution. In the following, we will explain several design considerations for HiF8 and show how those references guide our design.

- Dot field

Consideration : To avoid multi-float8 formats like HFP8 for deep learning, tapered precision is a promissing direction to explore. Posit realizes the tapered precision by adopting a variable-length field called regime to encode two base values of the exponents. However, the regime field using unary coding is not convenient and flexible enough to manipulate the significant bits distribution over the exponent to better match the training requirements.

Design : Therefore, HiF8 adopts the flexible prefix code to form a novel dot field, which directly indicates the width of exponent and the sign of denormal. Moreover, to smooth the precision variation and avoid the mantissa width jumping down by more than 1 bit, we use large width to code small numbers and small width to code large numbers. One can obtain an in-depth analysis from Table 1 and Table 2.

- Exponent field

Consideration : To avoid coding redundancy, we must ensure that the exponent values pointed by each value of the dot field do not overlap with each other. Coding methods like the offset-bianry used in FP16 and the special one used in Posit, cannot achieve this goal. Fortunately, there are other three signed number reprentations for us to consider: sign-magnitude, one's complement, and two's complement.

Design : Inspired by the implicit bit design of the mantissa field in FP16, HiF8 chooses the sign-magnitude coding for the exponent field, where one implicit bit is fixed to 1 to avoid repetitive representation of the exponent values. As shown in Table 3, HiF8 becomes non-redundant in data expression.

- Denormal Mode

Consideration : Without the denormal design, HiF8 would have a 4-bit mantissa when the exponent is equal to zero, but would only support 31 exponent values from -15 to 15. Currently, the activation gradients of LLMs require a higher dynamic range of the data format [30]. While from the practice of HFP8 or FP8, we can conclude that 3-bit mantissa is sufficient for training tasks. Thus a better balance is possible to extend the dynamic range of HiF8.

Design : We reduce the mantissa width from 4 bits to 3 bits when the exponent is equal to zero. Then the resulting free coding spaces are directly used to expand the exponent range, as formulated by the denormal euqation (2) and depicted in Fig. 1. In this way, the binades that HiF8 can cover increase from 31 to 38, very close to the 40 of FP16.

From the above analyses, we can see that HiF8 stands on the shoulders of the three data formats, absorbs their advantages, and finally achieves a better balance for deep learning at the 8-bit limit. Compared with FP8, HiF8 takes both precision and dynamic range into account, and is capable of replacing two formats of FP8 with only one format. Compared with Posit(8, 2) [27,28], HiF8 has 31 exponents with mantissa no less than 1 bit, while Posit(8, 2) only has 24 exponents with mantissa no less than 1 bit. And compared with FP16, HiF8 has almost the same dynamic range, which is much better than FP8-E4M3 and FP8-E5M2.

## 3 Rounding Methods

In Float8 mixed precision training and inference, high-precision floating-point formats such as FP32 need to be converted into low-precision format Float8, and then input to GEMM, during which rounding is involved. As the precision of Float8 is relatively lower than BF16 and FP16, the rounding method is extremely sensitive to the convergence and accuracy of neural network training. After the theoretical analysis and a large number of experiments, we conculde that HiF8 will support two rounding methds: rounding half to away (from zero), and hybrid rounding. To covert high-precision data to HiF8, we use only rounding half to away in the forward pass, and rounding half to away or hybrid rounding in the backward pass. In addition, to meet the requirements of certain AI algorithms, HiF8 also provides two options: saturation to boundary upon overflow, and NaN saturation to zero. The following describes the rounding methods during the conversion from high-preciosn formats to HiF8.

## 3.1 Rounding Half

Rounding half (rounding to nearest) yields an error of 0.5 ulp (unit of least precision), and can be generally classfied into rounding half to even (TE) and rounding half to away (TA) [14]. Technically, if the MSB of the discarded bits is 1 and the other discarded bits are all 0, TE would ensure that the LSB (least significant bit) of the rounded number is even by carrying or not. Otherwise, both TE and TA would carry as long as the MSB of the discarded bits is 1. Although TA features easier hardware implementation, TE is used by default in most papers and commercial products, because it maximizes the unbiasedness [22]. In fact, the occurrence probability of the TE special case is extremely low during the conversion from high-precision formats to HiF8. For example, if HiF8 reserves 3-bit mantissa, the probability is only 2 -20 during the conversion from FP32 to HiF8.

The biggest challenge of Float8 in AI is its limited data resolution capability. The analysis result shows that the data resolution capability of TA is slightly higher than that of TE. Consider a TE special case of three 3-bit numbers with consecutive integer bits: 00.1, 01.1, and 10.1. TE is rounded as TE(00.1) = 00, TE(01.1) = 10, TE(10.1) = 10, giving two different results. TA is rounded as TA(00.1) = 01, TA(01.1) = 10, TA(10.1) = 11, giving three different results. Therefore, in the TE special case, TA enables a higher data resolution capability of Float8 than TE. The simulation experiments of HiF8 also evidence that TA produces slightly higher training accuracy than TE. For example, the TA-based training accuracies of ResNet50 [31] and MobileNet\_V2 [32] are 0.06% and 0.11% higher than the TE-based training accuracies on average.

Since TA features simpler hardware implementation and higher training accuracy, it is therefore supported during the conversion from high-precision formats (including FP32, FP16, and BF16) to HiF8.

## 3.2 Hybrid Rounding

Large-scale HiF8 mixed precision training experiments show that global TA rounding works well for almost all neural networks. But for YoLo-V3-Tiny [33], some segments of the loss curve crashed. As a result, the final accuracy was 1.67% lower than the FP32 baseline. After extensive research and many experiments, in addition to the global TA rounding method, we propose a second HiF8 rounding method for training, which combines TA rounding for the forward pass and hybrid rounding for the backward pass. This makes the training accuracy of the YoLo-V3-Tiny close to the baseline value. Therefore, HiF8 supports both TA rounding and hybrid rounding (HR). In fact, HR is essentially an optimized version of standard stochastic rounding [34], which is easier to implement in circuits and has slightly better training accuracy.

The error of stochastic rounding (SR) is 1 ulp. Compared with TA, SR has a significant advantage when data is processed in batches. Specifically, in SR, a uniformly distributed random number needs to be randomly generated and used as threshold T, ( T ∈ [0 , 1)) . All bits to be discarded are regarded as fractional bits and marked as F, ( F ∈ [0 , 1)) . If F ≥ T , 1 is added to the reserved bits K, otherwise 0 is added to the reserved bits K. As threshold T is uniformly distributed, the expected value after SR is expressed as follows:

<!-- formula-not-decoded -->

Apparently, SR can maximize the invariance of the overall mean value during the rounding of batch data. However, deep learning needs to generate a large number of uniformly distributed random numbers in parallel, both software and hardware implementations of SR hit a performance bottleneck [35].

To tackle the bottleneck, we first come up with a simplified SR hardware solution. Theoretical analysis and experiments show that the lower mantissa bits of floating-point numbers obey uniform distribution. Therefore, for the FP32 source data, we set 14 LSBs of the source format as the threshold T14, and 14 MSBs of the discarded bits as the fractional bits F14. However, for FP16 and BF16 source data, the discarded bits are not wide enough to be divided into reasonable and weakly relevant threshold and fraction. To solve this dilemma, we combine a fixed 1 and the LSB of the source format into a special 2-bit threshold T2, and set the 2-bit MSBs of the discarded bits as the fractional bits F2. As illustrated in Fig. 2, we have designed a 14-bit SR (SR14) for FP32 and a 2-bit SR (SR2) for FP16 and BF16, without generating the random numbers by complex algorithms. SR14 is very similar to standard SR, with the same 1 ulp rounding error. SR2 is weakly stochastic with only 2 thresholds of 0.25 and 0.75, but has a small rounding error of 0.75 ulp. So far, by comparing F14/F2 with T14/T2, simplified SR can be done in hardware.

Figure 2: Threshold and Fraction of Simplified Stochastic Rounding

| Mantissa ofFP32   | Mantissa ofFP32                    | MantissaofFP16   | MantissaofFP16   | MantissaofFP16   | MantissaofBF16   | MantissaofBF16   | MantissaofBF16   | MantissaofBF16   | MantissaofBF16   | MantissaofBF16   |
|-------------------|------------------------------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|
| 01                | 2345678910111213141516171819202122 | 0                | 23               | 45678            | 9                | 0 1              | 23               | 456              | 7                |                  |
| M                 | F14                                | M                | F2               |                  | LSB              | M                | F2               |                  | LSB              |                  |
|                   | T14                                |                  | T2 ={LSB, 1'b1}  | T2 ={LSB, 1'b1}  | T2 ={LSB, 1'b1}  | T2 = {LSB,1'b1}  | T2 = {LSB,1'b1}  | T2 = {LSB,1'b1}  | T2 = {LSB,1'b1}  | T2 = {LSB,1'b1}  |

HiF8 training experiments show that the effect of simplified SR is quite close to that of standard SR, but there is still a very small gap. In fact, simplified SR achieves better mean invariance than TA, but incurs greater rounding error. Meanwhile, from Fig. 1 and the centralized characteristic of AI data, we can make the following logical inference. Most of the data is within the high-precision range of HiF8, in which TA rounding will cause only a small change in the average value, becuase the rounding direction is relatively balanced for large data volume. However, a small amount of data (especially large values) is within the low-precision range of HiF8, in which TA rounding may incur a large change in the average value , because the rounding direction can be unbalanced for small data volume. Through such analysis, we propose a hybrid rounding method as follows.

<!-- formula-not-decoded -->

In the HR rounding equation (3), E is the exponent value of the source data format. Experiments show that HR yields slightly better training accuray than the standard SR with low hardware cost. Especailly, for YoLo-V3-Tiny training, the baseline accuracy of FP16 mixed precsion is 16.63%. When using global TA rounding, the training accuracy of HiF8 is 14.96%, 1.67% lower than the baseline. When using TA rounding for the forward pass and standard SR for the backward pass, the training accuracy of HiF8 is 16.43%, 0.20% lower than the baseline. When using TA rounding for the forward pass and hybrid rounding for the backward pass, the training accuracy of HiF8 is 16.69%, slightly better than the baseline.

Thus, in addition to the TA rounding, the proposed hybrid rounding is also supported during the conversion from high-precision formats (including FP32, FP16, and BF16) to HiF8. Note that there is no need to use hybrid rounding in the forward pass, because the distribution of activations and weights is relatively more concentrated than the distribution of gradients in the backward pass. At the same time, for the vast majority of neural networks, training with TA and HR makes very little difference, and so far we have only found one neural network that definitely needs HR.

## 4 Experiments on Traditional Neural Networks

Currently, no hardware platform is available to support HiF8 data type and complete the computation process. Thus both training and inference experiments of traditional neural networks and LLMs, were performed with simulated HiF8 format. Specifically, using the rounding methods described above, the tensor values were converted from high-precision formats to only those that could be represented in HiF8. Hardware platforms, including Huawei Ascend NPUs [16,36] and NVDIA GPUs [15,37], and software framework PyTorch [38], were utilized to conduct the HiF8 training and inference experiments.

Since traditional neural networks and LLMs have been identified to have varying degrees of data dispersion, we handle them differently. In this section, only empirical results for the traditional neural networks are presented.

## 4.1 Training with Backward Loss-Scaling

As mentioned earlier, the dynamic range of HiF8 is almost the same as that of FP16, so for the traditional neural network, we inherit the training method of FP16 mixed precision. Specifically, only the GEMM inputs, including activation, weight, and activation gradient tensors, are changed from FP16 to HiF8 (excluding the last fully-connected layer). The others such as non-linearities or normalizations, remain the same as the FP16 mixed precision training. Most importantly, backward global loss-scaling is enabled to avoid excessive zero-valued gradients, which is the core trick to make both FP16 and HiF8 training effective [17]. As for the conversion from high-precision formats to HiF8, only TA rounding is used in the forward pass, and either TA rounding or hybrid rounding is used in the backward pass.

We trained FP16 baseline results and HiF8 results with the same model architectures, weight initializations (non-fixed random seeds), and optimizer hyper-parameters, and compared them. To verify the training accuracy of HiF8 for the traditional nerural networks, we chose two main application directions for simulation experiments: computer vision and natural language processing (NLP). The subdivided application scenarios of computer vision include classification, detection, and segmentation. In this paper, the most widely used typical networks based on the CNN and Transformer structures are selected for the experiments, including ResNet series [31], ResNeXt [39], VGG [40], MobileNet [32], Inception [41], EfficientNet [42], DenseNet [43], ViT series [44], YoLo series [33], and DeepLab [45]. For NLP, the mainstream Transformer models [46,47] are used.

Figure 3: Training Loss Curves for Traditional Neural Networks

![图2](images/page_001.png)

Fig. 3 compares the loss curves of HiF8 mixed precision training and FP16 mixed precision training (base) on the ResNet50, YoLo-V3-Tiny, ViT-Base, and Transformer-Base neural network models. The loss curves of HiF8 are highly overlapped with that of FP16, therefore the convergence speed of HiF8 is the same as that of FP16, and both HiF8 training and FP16 training can be completed within the same number of epochs.

Table 5: Validation Accuracy for Traditional Neural Networks

| Model             | Metric    |   FP16 | HiF8      | HiF8 - FP16   |
|-------------------|-----------|--------|-----------|---------------|
| DenseNet121       | Top-1 Acc |  76.04 | 75 . 93 ∗ | - 0 . 11      |
| EfficientNet-B0   | Top-1 Acc |  77.33 | 77 . 08   | - 0 . 25      |
| Inception-V3      | Top-1 Acc |  77.86 | 77 . 85 ∗ | - 0 . 01      |
| MobileNet-V2      | Top-1 Acc |  72.41 | 72 . 10   | - 0 . 31      |
| ResNet18          | Top-1 Acc |  70.78 | 70 . 64   | - 0 . 14      |
| ResNet34          | Top-1 Acc |  74.41 | 74 . 25   | - 0 . 16      |
| ResNet50          | Top-1 Acc |  77.36 | 77 . 39 ∗ | +0 . 03       |
| ResNet101         | Top-1 Acc |  78.84 | 78 . 78 ∗ | - 0 . 06      |
| ResNet152         | Top-1 Acc |  79.42 | 79 . 41   | - 0 . 01      |
| ResNeXt50         | Top-1 Acc |  78.14 | 78 . 01   | - 0 . 13      |
| VGG16             | Top-1 Acc |  74.07 | 74 . 02   | - 0 . 05      |
| VGG16-BN          | Top-1 Acc |  74.59 | 74 . 54   | - 0 . 05      |
| ViT-Base-Patch16  | Top-1 Acc |  79.05 | 79 . 18 ∗ | +0 . 13       |
| ViT-Base-Patch32  | Top-1 Acc |  74.09 | 74 . 08 ∗ | - 0 . 01      |
| ViT-Large-Patch16 | Top-1 Acc |  76.08 | 76 . 45 ∗ | +0 . 37       |
| ViT-Large-Patch32 | Top-1 Acc |  71.77 | 71 . 82 ∗ | +0 . 05       |
| Transformer-Base  | BLEU      |  25.92 | 26 . 04   | +0 . 12       |
| Bert-Large-MRPC   | F1        |  89.67 | 90 . 02   | +0 . 35       |
| YoLo-V3           | mAP50-95  |  43.70 | 43 . 60   | - 0 . 10      |
| YoLo-V3-Tiny      | mAP50-95  |  16.63 | 16 . 69 ∗ | +0 . 06       |
| DeepLab-V3        | mIOU      |  78.65 | 78 . 51 ∗ | - 0 . 14      |

∗ : Backward rounding for HiF8 is HR, otherwise TA

Experimental results for the traditional neural networks are listed in Table 5. Models from DenseNet to ViT series were all trained and evaluated on ImageNet ILSVRC2012 dataset. Transformer-Base was trained on WMT 2016 English -&gt; German dataset and tested on newstest2014 dataset. Bert-Large was trained and evaluated on GELU MRPC dataset. YoLo series were trained and tested on COCO2017 dataset. And DeepLab-V3 was trained and evaluated on PASCAL VOC2012 dataset. For all metrics in Table 5, higher scores are better. To smooth the jitter and deviation caused by weight initialization, the validation accuracy of some models was the average value of 2 to 4 rounds of training for both FP16 and HiF8. As for the validation accuracy of training using TA rounding and hybrid rounding, we only presented the results with higher accuracy. However, only Yolo-V3-Tiny shows a significant difference in the validation accuracy of the two rounding methods.

From Table 5, we can see that for the CNN structure, HiF8 shows slightly lower training accuray than FP16. For the Transformer structure, HiF8 shows slightly higher training accuracy than FP16. In general, for the traditional neural networks, we conclude that HiF8 training results with backward global loss-scaling strategy, match those of FP16 training sessions. This is better than the FP8 training method, which requires per-tensor scaling due to the narrow dynamic range [22].

## 4.2 Inference with Per-Tensor Scaling

The model trained by HiF8 can be directly used for inference. Therefore, this section only focuses on the process of converting high-precision trained model into HiF8 inference model. To reflect the capability of HiF8, two inference results of post-training quantization (PTQ) will be presented. First, we directly cast high-precision activation and weight tensors of all layers into HiF8 format without calibration, and compare its accuray with the original model. Second, we evaluate HiF8 calibration of models trained in FP32 or FP16. Unlike the int8 and FP8 calibration, which usually use per-tensor scaling for activations and per-channel scaling for weights [22, 48], in this paper, we only perform the per-tensor scaling for both activations and weights of all layers.

## Algorithm 1 HiF8 Calibration with Per-Tensor Scaling

```
Input: Calibration Dataset, High-Precision Model M Output: HiF8 Quantized Model 1: for l in 1 st to L th layer in M do 2: Forward & Collect high-precision output of layer l : O l = A l × W l 3: end for 4: Initialize O 0 q with calibration dataset 5: for l in 1 st to L th layer in M do 6: for Ea = [ -4 , 5] do 7: for Ew = [ -4 , 5] do 8: Scale & Cast: A l q = To_HiF8_TA( O l -1 q × 2 Ea ), W l q = To_HiF8_TA( W l × 2 Ew ) 9: MatMul & Restore: O l q = ( A l q × W l q ) × 2 -( Ea + Ew ) 10: Quantization Error: Err l = MSE ( O l q , O l ) 11: end for 12: end for 13: Find min ( Err l ) of all search space & Store the corresponding Ea , and Ew 14: Vector operations (Non-linearities & Normalizations): O l q = V ector ( O l q ) 15: end for
```

As shown in Algorithm 1, we restrict the value of each tensor's scaling factor to an integer power of two. In this way, there are only a limited number of proper choices for scaling factors near 2 0 , and the scaling operations involve only addition and subtraction of exponents, no multiplication. To find two suitable scaling factors for a tensor multiplication inputs, we search for several combinations of scaling factors and choose the result that minimizes the MSE (mean squared error) of the output tensor.

Table 6: Validation Accuracy after HiF8 PTQ of Traditional Neural Networks

| Model                | Metric    | Baseline   |   HiF8_Cast | Cast - Baseline   | HiF8_PTS   | PTS - Baseline   |
|----------------------|-----------|------------|-------------|-------------------|------------|------------------|
| ResNet18             | Top-1 Acc | 69.76      |       68.98 | - 0 . 78          | 69.48      | - 0 . 28         |
| ResNet34             | Top-1 Acc | 73.31      |       72.56 | - 0 . 76          | 72.96      | - 0 . 35         |
| ResNet50             | Top-1 Acc | 76.13      |       74.85 | - 1 . 28          | 75.44      | - 0 . 69         |
| ResNet101            | Top-1 Acc | 77.37      |       76.48 | - 0 . 89          | 76.89      | - 0 . 48         |
| ResNet152            | Top-1 Acc | 78.31      |       77.76 | - 0 . 55          | 77.96      | - 0 . 35         |
| ResNeXt50            | Top-1 Acc | 77.62      |       76.74 | - 0 . 88          | 77.17      | - 0 . 44         |
| VGG16                | Top-1 Acc | 71.59      |       70.98 | - 0 . 61          | 71.28      | - 0 . 31         |
| DenseNet121          | Top-1 Acc | 74.43      |       73.58 | - 0 . 86          | 74.14      | - 0 . 29         |
| Inception-V3         | Top-1 Acc | 77.92      |       76.67 | - 1 . 25          | 77.38      | - 0 . 54         |
| ViT-Base-Patch16     | Top-1 Acc | 81.07      |       80.86 | - 0 . 21          | 80.91      | - 0 . 15         |
| ViT-Base-Patch32     | Top-1 Acc | 75.92      |       75.66 | - 0 . 26          | 75.85      | - 0 . 07         |
| ViT-Large-Patch16    | Top-1 Acc | 79.68      |       79.69 | +0 . 00           | 79.77      | +0 . 09          |
| ViT-Large-Patch32    | Top-1 Acc | 76.96      |       76.83 | - 0 . 13          | 76.87      | - 0 . 09         |
| MaskRCNN             | bbox      | 37.8       |        37.1 | - 0 . 7           | 37.3       | - 0 . 5          |
| SSD-VGG16            | bbox      | 25.1       |        24.2 | - 0 . 9           | 24.8       | - 0 . 3          |
| YoLo-V3              | mAP50-95  | 43 . 3 ∗   |        42.2 | - 1 . 1           | 42.8       | - 0 . 5          |
| 3D-Unet              | mean-dice | 90 . 98 ∗  |       91.03 | +0 . 05           | /          | /                |
| Bert-Large-MRPC      | F1        | 87 . 44 ∗  |       87.19 | - 0 . 25          | 87.63      | +0 . 19          |
| Bert-Large-SQuADv1.1 | F1        | 91 . 40 ∗  |       91.39 | - 0 . 01          | /          | /                |

HiF8\_Cast: Directly cast F32/16 tensors to HiF8

HiF8\_PTS: Calibration with Per-tensor Scaling

Table 6 lists the inference results of HiF8 for the traditional neural networks. In addition to some of the previously mentioned models, we further evaluated the inference accuracy of MaskRCNN [49] and SSD-VGG16 [50] in detection applications, as well as the 3D-Unet [51] in segmentation scenarios. For all metrics in Table 6, higher scores are better. We define the metric loss of no greater than 0.5 as the ideal inference result, and mark it blue. It can be seen that Transformer-based models can be used for inference after direct conversion to HiF8 without calibration. When per-tensor scaling is enabled for both activations and weights, most CNNs can be used for inference.

To improve HiF8 inference accuracy for the traditional neural networks, two further methods can be tried. First, based on per-tensor scaling for both activations and weights, we can leave some sensitive layers as FP16 or BF16. For example, if we convert the first layer of ResNet50 and Inception-V3 to FP16 and the other layers to HiF8, their accuracy losses improve to be 0 . 20 and 0 . 23 . Second, like int8 and FP8, we can use per-tensor scaling for activations and per-channel scaling for weights.

## 5 Experiments on Large Language Models

LLMs exhibit some unique features that differ from the traditional neural networks. On the training side, the gradients distribution is more dispersed. Thus larger dynamic range or special technique, is required to avoid too much data becoming zero during data type conversion [52] . In terms of inference, outliers play an important role in validation accuracy. Therefore, dedicated method such as SmoothQuant [53], is possible needed to reduce the quantization error of outliers. In this section, to apply HiF8 on LLMs, we proposed and tried three training methods, each with different costs and coverage. We also evaluated three inference methods, including direct-cast, per-tensor scaling, and SmoothQuant. Note that for LLMs, only TA rounding was used for HiF8.

## 5.1 Training

First, we inroduce the HiF8 training methods for LLMs in our experiments:

## · Backward Loss-Scaling (BLS)

This method is inherited from FP16 mixed-precision training [17]. More details can be found in Section 4.1.

## · Adaptive Loss-Scaling (ALS)

This is an optimal configuration for the backward loss-scaling. In the current mixed-precision training, scale window (growth\_interval) is an input constant throughout the training task 2 , and is usually set to 1000 or 2000 for the traditional neural networks. In some LLMs, the maginitude of gradients changes rapidly in the early iterations. At this moment, large scale window cannot catch up with the change in gradients, resulting in a failure of convergence. However, a scale window that is too small can significantly degrade the performance of training.

To address this dilemma, we propose the adaptive loss-scaling. Specifically, we first define an incremental list of scale window, such as {1, 20, 50, 100, 200, 500, 1000}. Then the inital scale value and scale window are set to 2 32 and 20. During training, if the scale value increases three times, the scale window will increase once as per the list order. If the scale value decreases three times in a row, scale window will decrease once as per the list order. The proposed ALS can be applied to both FP16 and HiF8 to improve the stability of training. Please refer to the website for more information 3 .

## · Per-Tensor Scaling (PTS)

Although training with BLS and ALS can be successfully carried out in HiF8 for a number of LLMs, there are cases where per-tensor scaling is needed to improve accuracy and mitigate the difficulty of hyper-parameters tuning. To be specific, we define a scale factor for each GEMM input tensor, including activation, weight, and activation gradient. The initial scale factors are all set to 1. Then every 10 iterations, we compute the maximun absolute value (Amax) of each tensor, and update the corresponding scale factor by a certain algorithm. To avoid additional rounding errors, the scale factors are restricted to integer powers of 2. While in each iteration, whether the scale factors are updated or not, they will scale the corresponding tensors to a better range that can be represented by HiF8. Finally, GEMM outputs need to be descaled to restore the correct results. Note that scale and descale operations are all carried out in high-precision formats, such as FP32, BF16, and FP16 (with BLS or ALS).

Actually, the PTS we used for HiF8 is very similar to the transformer engine for FP8 [52]. However, because HiF8 has much larger dynamic range than FP8 (especially E4M3), we do not need to compute Amax in all iterations, thereby greatly reducing the occupation of vector resources.

In the training experiments for LLMs, we selceted T5 [54], LLaMA [55], and GPT3 [56] to evidence the capability of HiF8. Our training datasets are several mixtures of three sources, including Book3 (101 GB) and OpenWebText2 (63 GB) from the Pile dataset [57], and Wikipedia (20 GB).

In Fig. 4, the training loss (average of every 10 iterations) over tokens is displayed for LLaMA-7B and GPT3 models of 6.7B and 13B parameters. The weight initializations (non-fixed random seeds) and optimizer hyper-parameters are consistent across models trianed with HiF8 and FP16. Again, only GEMM inputs, including activation, weight, and activation gradient tensors, are casted from FP16 to HiF8. As shown in Fig. 4, from a global view, the loss curves overlap with each other very well. And from a locally enlarged view, we can see that the difference between HiF8 and FP16 is within run-to-run variation caused by different random seeds.

[2 https://pytorch.org/docs/stable/\_modules/torch/cuda/amp/grad\_scaler.html](https://pytorch.org/docs/stable/_modules/torch/cuda/amp/grad_scaler.html)

[3 https://mindformers.readthedocs.io/zh-cn/latest/docs/feature\_cards/Training\_Algorithms.html](https://mindformers.readthedocs.io/zh-cn/latest/docs/feature_cards/Training_Algorithms.html)

Figure 4: Training Loss Curves for Large Language Models

![图3](images/page_002.png)

Validation perplexities (PPL: lower is better) for a variety of LLMs are listed in Table 7. FP16 baselines are all trained with BLS strategy. From Table 7, we can conclude that HiF8 traning results for LLMs, match those of FP16 training sessions. Specifically, with very small penalty of training accuray, HiF8 with BLS or ALS has almost no extra overhead compared to the FP16 baseline. While ALS technique can obviously mitigate the difficulty of hyper-parameters tuning, such as the ratio of warmup iterations.

Table 7: Validation Perplexity for Large Language Models

| Model     | Training Data        | Training Tokens   | HiF8 Strategy   |   FP16 |   HiF8 | HiF8 - FP16   |
|-----------|----------------------|-------------------|-----------------|--------|--------|---------------|
| T5-11B    | Wiki                 | 3.28B             | BLS             |   7.40 |   7.53 | +0 . 13       |
| GPT3-350M | Wiki, OpenWeb, Book3 | 14.8B             | BLS             |  17.43 |  17.52 | +0 . 09       |
| GPT3-2.7B | Wiki, OpenWeb, Book3 | 10.5B             | BLS             |  14.96 |  15.04 | +0 . 08       |
| GPT3-6.7B | Wiki, OpenWeb, Book3 | 21.3B             | ALS             |  13.06 |  13.14 | +0 . 08       |
| GPT3-6.7B | Wiki, OpenWeb, Book3 | 21.3B             | ALS + PTS       |  13.06 |  12.99 | - 0 . 07      |
| GPT3-13B  | Wiki, OpenWeb, Book3 | 14.8B             | ALS + PTS       |  12.62 |  12.54 | - 0 . 08      |
| LLaMA-7B  | Wiki, OpenWeb        | 14.8B             | ALS + PTS       |   8.25 |   8.28 | +0 . 03       |
| LLaMA-13B | Wiki, OpenWeb        | 8.85B             | ALS + PTS       |   8.71 |   8.74 | +0 . 03       |

Meanwhile, with the extra computation of Amax every 10 iterations, HiF8 with PTS strategy sometimes yields better training accuracy than the FP16 baseline. Fortunately, thanks to the large daynamic range of HiF8, such additional overhaed is much smaller than the FP8 with transformer engine [52], resulting in better training performance on some neural networks.

## 5.2 Inference

The LLM trained by HiF8 can be directly used for inference. Thus we only consider the HiF8 PTQ of LLMs trained in higher precision. In addition to the PTQ methods of direct-cast and per-tensor scaling used in Section 4.2, we further evaluated the SmoothQuant [53] calibration method for LLMs, due to the influence of outliers. First, to objectively reflect the inference ability of HiF8, we chose the quantization-tolerant LLaMA [55], and the quantization-sensitive OPT [58] as the experimental LLMs.

Table 8: WikiText2 Perplexity after HiF8 PTQ of Large Language Models

| Model     |   FP16 |   HiF8_Cast |   Cast - FP16 |   HiF8_PTS |   PTS - FP16 |   HiF8_SQ |   SQ - FP16 |
|-----------|--------|-------------|---------------|------------|--------------|-----------|-------------|
| LLaMA-7B  |   5.00 |        5.06 |          0.06 |       5.02 |         0.02 |      5.02 |        0.02 |
| LLaMA-13B |   4.54 |        4.60 |          0.06 |       4.55 |         0.01 |      4.58 |        0.04 |
| LLaMA-65B |   3.13 |        3.16 |          0.03 |       3.16 |         0.03 |      3.16 |        0.03 |
| OPT-7B    |   9.08 |       10.68 |          1.60 |       9.54 |         0.46 |      9.38 |        0.30 |
| OPT-13B   |   8.64 |        9.11 |          0.47 |       9.08 |         0.44 |      8.72 |        0.08 |
| OPT-66B   |   7.74 |       106.9 |         99.16 |       8.16 |         0.42 |      7.92 |        0.18 |

HiF8\_Cast: Directly cast F32/16 tensors to HiF8

HiF8\_PTS: Calibration with Per-tensor Scaling

HiF8\_SQ: Calibration with SmoothQuant

As shown in Table 8, for some quantization-tolerant LLMs such as LLaMA, HiF8 can easily achieve the desired inference accuracy even if only the simplest direct-cast is performed. But for some quantization-sensitive LLMs like OPT, dedicated calibration methods, such as PTS and SmoothQuant, are needed to improve the inference accuray of HiF8. More PTS calibration results for downstream tasks are outlined in Table 9.

Table 9: Inference Accuracy after HiF8 PTS Calibration for Large Language Models

| Model     | Downstream Task   | Metric              |   FP16 |   HiF8 | Metric Loss   |
|-----------|-------------------|---------------------|--------|--------|---------------|
| GPT3-2.7B | MMLU              | Acc_Avg (5-shots) ↑ |  27.73 |  27.90 | - 0 . 17      |
| GPT3-2.7B | WikiText103       | PPL ↓               |  12.05 |  12.20 | +0 . 15       |
| LLaMA-7B  | Lambada           | Acc (zero-shot) ↑   |  89.37 |  89.21 | +0 . 16       |

Finally, as described in Section 4.2, per-tensor scaling for activations and per-channel scaling for weights, and some combination of different calibration methods, are worth trying to further improve the HiF8 inference accuracy of LLMs.

## 6 Conclusion and Outlook

In this preliminary white paper, we propose a novel 8-bit floating-point format HiFloat8, consisting of sign, dot, exponent, and mantissa fields. By deeply exploring the match between format and data distribution, HiF8 achieves a much better balance between precision and daynamic range than the existing 8-bit formats. Experments on a large number of traditional neural networks and LLMs, demonstrate that as a single format, HiF8 works well in both training and inference. In the future, we will disclose another research achievement of HiFloat project: HiFloat below 8-bit, as well as its training and inference capabilities.

## References

- [1] M. Golio, 'Fifty years of moore's law,' Proc. IEEE , vol. 103, no. 10, pp. 1932-1937, 2015.
- [2] Y. Kwon and M. Rhu, 'Beyond the memory wall: A case for memory-centric hpc system for deep learning,' in 2018 51st Annual IEEE/ACM International Symposium on Microarchitecture (MICRO) , pp. 148-161, IEEE, 2018.
- [3] S. Linnainmaa, Alogritmin kumulatiivinen pyöristysvirhe yksittäisten pyöristysvirheiden Taylor-kehitelmänä . PhD thesis, University of Helsinki, 1970.
- [4] Y. LeCun, Y. Bengio, et al. , 'Convolutional networks for images, speech, and time series,' The handbook of brain theory and neural networks , vol. 3361, no. 10, p. 1995, 1995.
- [5] S. Hochreiter and J. Schmidhuber, 'Long short-term memory,' Neural Computation , vol. 9, pp. 1735-1780, 11 1997.
- [6] I. S. Board, 'Ieee standard for binary floating-point arithmetic,' ANSI/IEEE Std 754-1985 , pp. 1-20, 1985.
- [7] K. Chellapilla, S. Puri, and P. Simard, 'High performance convolutional neural networks for document processing,' in Tenth international workshop on frontiers in handwriting recognition , Suvisoft, 2006.
- [8] D. Nuzman, I. Rosen, and A. Zaks, 'Auto-vectorization of interleaved data for simd,' ACM SIGPLAN Notices , vol. 41, no. 6, pp. 132-143, 2006.
- [9] A. Krizhevsky, I. Sutskever, and G. E. Hinton, 'Imagenet classification with deep convolutional neural networks,' Advances in neural information processing systems , vol. 25, 2012.
- [10] M. Abadi, A. Agarwal, et al. , 'Tensorflow: Large-scale machine learning on heterogeneous distributed systems,' CoRR , vol. abs/1603.04467, 2016.
- [11] D. Kalamkar, D. Mudigere, N. Mellempudi, D. Das, K. Banerjee, S. Avancha, D. T. Vooturi, N. Jammalamadaka, J. Huang, H. Yuen, et al. , 'A study of bfloat16 for deep learning training,' arXiv preprint arXiv:1905.12322 , 2019.
- [12] N. P. Jouppi, C. Young, N. Patil, D. Patterson, G. Agrawal, R. Bajwa, S. Bates, S. Bhatia, N. Boden, A. Borchers, et al. , 'In-datacenter performance analysis of a tensor processing unit,' in Proceedings of the 44th annual international symposium on computer architecture , pp. 1-12, 2017.
- [13] D. Silver, J. Schrittwieser, K. Simonyan, I. Antonoglou, A. Huang, A. Guez, T. Hubert, L. Baker, M. Lai, A. Bolton, et al. , 'Mastering the game of go without human knowledge,' nature , vol. 550, no. 7676, pp. 354-359, 2017.
- [14] D. Zuras, M. Cowlishaw, A. Aiken, M. Applegate, D. Bailey, S. Bass, D. Bhandarkar, M. Bhat, D. Bindel, S. Boldo, et al. , 'Ieee standard for floating-point arithmetic,' IEEE Std , vol. 754, no. 2008, pp. 1-70, 2008.
- [15] S. Markidis, S. W. Der Chien, E. Laure, I. B. Peng, and J. S. Vetter, 'Nvidia tensor core programmability, performance &amp; precision,' in 2018 IEEE international parallel and distributed processing symposium workshops (IPDPSW) , pp. 522-531, IEEE, 2018.
- [16] H. Liao, J. Tu, J. Xia, and X. Zhou, 'Davinci: A scalable architecture for neural network computing.,' in Hot Chips Symposium , pp. 1-44, 2019.

- [17] P. Micikevicius, S. Narang, J. Alben, G. Diamos, E. Elsen, D. Garcia, B. Ginsburg, M. Houston, O. Kuchaiev, G. Venkatesh, et al. , 'Mixed precision training,' arXiv preprint arXiv:1710.03740 , 2017.
- [18] N. Wang, J. Choi, D. Brand, C.-Y. Chen, and K. Gopalakrishnan, 'Training deep neural networks with 8-bit floating point numbers,' Advances in neural information processing systems , vol. 31, 2018.
- [19] X. Sun, J. Choi, C.-Y. Chen, N. Wang, S. Venkataramani, V. V. Srinivasan, X. Cui, W. Zhang, and K. Gopalakrishnan, 'Hybrid 8-bit floating point (hfp8) training and inference for deep neural networks,' Advances in neural information processing systems , vol. 32, 2019.
- [20] A. Agrawal, S. K. Lee, J. Silberman, M. Ziegler, M. Kang, S. Venkataramani, N. Cao, B. Fleischer, M. Guillorn, M. Cohen, et al. , 'A 7nm 4-core ai chip with 25.6 tflops hybrid fp8 training, 102.4 tops int4 inference and workload-aware throttling. in 2021 ieee international solid-state circuits conference (isscc),' 2021.
- [21] A. C. Elster and T. A. Haugdahl, 'Nvidia hopper gpu and grace cpu highlights,' Computing in Science &amp; Engineering , vol. 24, no. 2, pp. 95-100, 2022.
- [22] P. Micikevicius, D. Stosic, N. Burgess, M. Cornea, P. Dubey, R. Grisenthwaite, S. Ha, A. Heinecke, P. Judd, J. Kamalu, et al. , 'Fp8 formats for deep learning,' arXiv preprint arXiv:2209.05433 , 2022.
- [23] B. D. Rouhani, R. Zhao, A. More, M. Hall, A. Khodamoradi, S. Deng, D. Choudhary, M. Cornea, E. Dellinger, K. Denolf, et al. , 'Microscaling data formats for deep learning,' arXiv preprint arXiv:2310.10537 , 2023.
- [24] A. Sabbagh Molahosseini, L. Sousa, A. A. Emrani Zarandi, and H. Vandierendonck, 'Low-precision floating-point formats: From general-purpose to application-specific,' Approximate Computing , pp. 77-98, 2012.
- [25] J. L. Gustafson and I. T. Yonemoto, 'Beating floating point at its own game: Posit arithmetic,' Supercomputing frontiers and innovations , vol. 4, no. 2, pp. 71-86, 2017.
- [26] J. Lu, S. Lu, Z. Wang, C. Fang, J. Lin, Z. Wang, and L. Du, 'Training deep neural networks using posit number system,' in 2019 32nd IEEE International System-on-Chip Conference (SOCC) , pp. 62-67, IEEE, 2019.
- [27] J. Lu, C. Fang, M. Xu, J. Lin, and Z. Wang, 'Evaluations on deep neural networks training using posit number system,' IEEE Transactions on Computers , vol. 70, no. 2, pp. 174-187, 2020.
- [28] G. Raposo, P. Tomás, and N. Roma, 'Positnn: Training deep neural networks with mixed low-precision posit,' in ICASSP 2021-2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) , pp. 7908-7912, IEEE, 2021.
- [29] S. Narang, G. Diamos, E. Elsen, P. Micikevicius, J. Alben, D. Garcia, B. Ginsburg, M. Houston, O. Kuchaiev, G. Venkatesh, et al. , 'Mixed precision training,' in Int. Conf. on Learning Representation , 2017.
- [30] S. P. Perez, Y. Zhang, J. Briggs, C. Blake, J. Levy-Kramer, P. Balanca, C. Luschi, S. Barlow, and A. W. Fitzgibbon, 'Training and inference of large language models using 8-bit floating point,' 2023.
- [31] K. He, X. Zhang, S. Ren, and J. Sun, 'Deep residual learning for image recognition,' in Proceedings of the IEEE conference on computer vision and pattern recognition , pp. 770-778, 2016.
- [32] M. Sandler, A. Howard, M. Zhu, A. Zhmoginov, and L.-C. Chen, 'Mobilenetv2: Inverted residuals and linear bottlenecks,' in Proceedings of the IEEE conference on computer vision and pattern recognition , pp. 4510-4520, 2018.
- [33] J. Redmon and A. Farhadi, 'Yolov3: An incremental improvement,' arXiv preprint arXiv:1804.02767 , 2018.
- [34] M. P. Connolly, N. J. Higham, and T. Mary, 'Stochastic rounding and its probabilistic backward error analysis,' SIAM Journal on Scientific Computing , vol. 43, no. 1, pp. A566-A585, 2021.
- [35] P. L'Ecuyer, 'History of uniform random number generation,' in 2017 Winter Simulation Conference (WSC) , pp. 202-230, IEEE, 2017.
- [36] R. Wu, M. Li, H. Li, T. Chen, X. Tian, X. Xu, B. Zhou, J. Chen, and H. An, 'Machine learning-enabled performance model for dnn applications and ai accelerator,' in 2022 IEEE 24th Int Conf on High Performance Computing &amp; Communications; 8th Int Conf on Data Science &amp; Systems , pp. 25-34, IEEE, 2022.
- [37] J. Choquette and W. Gandhi, 'Nvidia a100 gpu: Performance &amp; innovation for gpu computing,' in 2020 IEEE Hot Chips 32 Symposium (HCS) , pp. 1-43, IEEE Computer Society, 2020.
- [38] A. Paszke, S. Gross, F. Massa, A. Lerer, J. Bradbury, G. Chanan, T. Killeen, Z. Lin, N. Gimelshein, L. Antiga, et al. , 'Pytorch: An imperative style, high-performance deep learning library,' Advances in neural information processing systems , vol. 32, 2019.
- [39] S. Xie, R. Girshick, P. Dollár, Z. Tu, and K. He, 'Aggregated residual transformations for deep neural networks,' in Proceedings of the IEEE conference on computer vision and pattern recognition , pp. 1492-1500, 2017.
- [40] K. Simonyan and A. Zisserman, 'Very deep convolutional networks for large-scale image recognition,' arXiv preprint arXiv:1409.1556 , 2014.
- [41] C. Szegedy, V. Vanhoucke, S. Ioffe, J. Shlens, and Z. Wojna, 'Rethinking the inception architecture for computer vision,' in Proceedings of the IEEE conference on computer vision and pattern recognition , pp. 2818-2826, 2016.

- [42] M. Tan and Q. Le, 'Efficientnet: Rethinking model scaling for convolutional neural networks,' in International conference on machine learning , pp. 6105-6114, PMLR, 2019.
- [43] G. Huang, Z. Liu, L. Van Der Maaten, and K. Q. Weinberger, 'Densely connected convolutional networks,' in Proceedings of the IEEE conference on computer vision and pattern recognition , pp. 4700-4708, 2017.
- [44] A. Dosovitskiy, L. Beyer, A. Kolesnikov, D. Weissenborn, X. Zhai, T. Unterthiner, M. Dehghani, M. Minderer, G. Heigold, S. Gelly, et al. , 'An image is worth 16x16 words: Transformers for image recognition at scale,' arXiv preprint arXiv:2010.11929 , 2020.
- [45] L.-C. Chen, G. Papandreou, F. Schroff, and H. Adam, 'Rethinking atrous convolution for semantic image segmentation,' arXiv preprint arXiv:1706.05587 , 2017.
- [46] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, Ł. Kaiser, and I. Polosukhin, 'Attention is all you need,' Advances in neural information processing systems , vol. 30, 2017.
- [47] J. D. M.-W. C. Kenton and L. K. Toutanova, 'Bert: Pre-training of deep bidirectional transformers for language understanding,' in Proceedings of naacL-HLT , vol. 1, p. 2, 2019.
- [48] M. Anderson, B. Chen, S. Chen, S. Deng, J. Fix, M. Gschwind, A. Kalaiah, C. Kim, J. Lee, J. Liang, et al. , 'First-generation inference accelerator deployment at facebook,' arXiv preprint arXiv:2107.04140 , 2021.
- [49] K. He, G. Gkioxari, P. Dollár, and R. Girshick, 'Mask r-cnn,' in Proceedings of the IEEE international conference on computer vision , pp. 2961-2969, 2017.
- [50] W. Liu, D. Anguelov, D. Erhan, C. Szegedy, S. Reed, C.-Y. Fu, and A. C. Berg, 'Ssd: Single shot multibox detector,' in Computer Vision-ECCV 2016: 14th European Conference, Amsterdam, The Netherlands, October 11-14, 2016, Proceedings, Part I 14 , pp. 21-37, Springer, 2016.
- [51] Ö. Çiçek, A. Abdulkadir, S. S. Lienkamp, T. Brox, and O. Ronneberger, '3d u-net: learning dense volumetric segmentation from sparse annotation,' in Medical Image Computing and Computer-Assisted Intervention-MICCAI 2016: 19th International Conference, Athens, Greece, October 17-21, 2016, Proceedings, Part II 19 , pp. 424-432, Springer, 2016.
- [52] J. Choquette, 'Nvidia hopper gpu: Scaling performance,' in 2022 IEEE Hot Chips 34 Symposium (HCS) , pp. 1-46, IEEE Computer Society, 2022.
- [53] G. Xiao, J. Lin, M. Seznec, H. Wu, J. Demouth, and S. Han, 'Smoothquant: Accurate and efficient post-training quantization for large language models,' in International Conference on Machine Learning , pp. 38087-38099, PMLR, 2023.
- [54] C. Raffel, N. Shazeer, A. Roberts, K. Lee, S. Narang, M. Matena, Y. Zhou, W. Li, et al. , 'Exploring the limits of transfer learning with a unified text-to-text transformer,' Journal of machine learning research , vol. 21, no. 140, pp. 1-67, 2020.
- [55] H. Touvron, T. Lavril, G. Izacard, X. Martinet, M.-A. Lachaux, T. Lacroix, B. Rozière, N. Goyal, E. Hambro, F. Azhar, et al. , 'Llama: Open and efficient foundation language models,' arXiv preprint arXiv:2302.13971 , 2023.
- [56] T. Brown, B. Mann, N. Ryder, M. Subbiah, J. D. Kaplan, et al. , 'Language models are few-shot learners,' Advances in neural information processing systems , vol. 33, pp. 1877-1901, 2020.
- [57] L. Gao, S. Biderman, S. Black, L. Golding, T. Hoppe, C. Foster, J. Phang, H. He, A. Thite, N. Nabeshima, S. Presser, and C. Leahy, 'The pile: An 800gb dataset of diverse text for language modeling,' CoRR , vol. abs/2101.00027, 2021.
- [58] S. Zhang, S. Roller, N. Goyal, M. Artetxe, M. Chen, S. Chen, C. Dewan, M. Diab, X. Li, X. V. Lin, et al. , 'Opt: Open pre-trained transformer language models,' arXiv preprint arXiv:2205.01068 , 2022.