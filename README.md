# muse-skills — 技能網

每個 skill 是一個可重用的能力模組；[SKILL_NET.md](SKILL_NET.md) 是整張網：
節點（skill）＋ 邊（互補 / fallback / 工作流）＋ 高頻迴路。

## 維護規則
1. 新 skill 上線先回答：補哪個缺口？跟誰互補？進哪條迴路？
2. Fallback 寫死，不靠臨場想
3. 錢、帳號、授權、公開發布四節點永遠是人工閘門
4. API key 等祕密只放本地 `.env`（已 gitignore），絕不進 repo
