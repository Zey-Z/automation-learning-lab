//read raw leads (看了笔记)
const fs = require("fs")
const rawLeads = fs.readFileSync("exercises/week-01/raw-leads.json", "UTF-8")
//parse，因为rawLeads是一个数组中包含很多对象的，而不是每条都是独立JSON，所以可以直接parse，不用map逐条
const leads = JSON.parse(rawLeads)  

//过滤符合条件的
const validLeads = leads.filter(l => l.score >= 70 && l.email.trim())

//操作和生成新的储存结果的对象
const result = validLeads.map(l => ({
    name:l.name,
    email:l.email.trim().toLowerCase(), 
    grade: l.score >= 90? "A": l.score >=80 ? "B":"C"
}))

//检查结果
console.log(result)

//读写文件我都要看下笔记，还不熟练
fs.writeFileSync("exercises/week-01/practice-f1-output.json", JSON.stringify(result, null, 2))




