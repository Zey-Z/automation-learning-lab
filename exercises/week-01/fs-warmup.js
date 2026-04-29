const fs = require("fs")//require 就是node js里面有的一个特定的东西，“fs”之所以是字符串意思是让require去找一个名字叫做“fs”的工具？

const raw = fs.readFileSync("exercises/week-01/test-input.json","utf-8")

const data = JSON.parse(raw)

console.log(data.company)

fs.writeFileSync("exercises/week-01/test-output.json",JSON.stringify(data.employees, null, 2))