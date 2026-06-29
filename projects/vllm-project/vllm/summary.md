# vllm

> [`vllm-project/vllm`](https://github.com/vllm-project/vllm) · 上游贡献

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · commit `0e207dac` · Python · 5684文件/? · 83,139n/490,393e  
<!-- END AUTO -->

---

## 定位
> 大语言模型高性能推理引擎，通过 PagedAttention 算法实现 KV cache 近零浪费（96%+ 利用率），吞吐量 2-4× 超越同类系统。SOSP 2023 论文支撑，LLM 推理领域标杆项目。

## 项目介绍
> 高性能 LLM 推理引擎。核心场景：(1) 大模型在线推理服务部署 (2) 通过 PagedAttention 实现接近零浪费的 KV cache 管理 (3) 支持 continuous batching 的多 GPU 分布式推理。13B 模型在 A100 上仅 4% KV cache 浪费。

## 技术栈
- Python · Git · Docker · CI/CD

## 关联
- [`vllm-project/pagedattention`](../../references/vllm-project/pagedattention/) — 奠基论文 (SOSP 2023)
- [`cosdt/vllm-ascend`](../../cosdt/vllm-ascend/) — 昇腾后端移植
- [`vllm-project/vllm-ascend`](../../vllm-project/vllm-ascend/) — 上游官方 Ascend 后端
- [`opensourceways/vLLM-dashboard-website`](../../opensourceways/vLLM-dashboard-website/) — 推理性能看板

## 开放问题
> _随 delta 追加_

