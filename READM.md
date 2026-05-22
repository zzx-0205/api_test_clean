# 接口自动化测试框架 (API Test Framework)

基于 **Python + Requests + Pytest** 的轻量级接口自动化测试项目，以 [JSONPlaceholder](https://jsonplaceholder.typicode.com) 作为被测服务，实现对文章资源的 **增删改查（CRUD）** 自动化回归测试。

## 🛠 技术栈

| 技术 | 说明 |
|------|------|
| Python 3.8+ | 开发语言 |
| Requests | HTTP 请求库，封装 Session 管理 |
| Pytest | 测试框架，fixture + parametrize |
| JSONPlaceholder | 被测 RESTful API（稳定、免费、无需鉴权） |
| Postman | 手工接口调试，导出集合文件 |
| GitHub Actions | 持续集成，自动运行测试 |

## 📂 项目结构