const fs = require("fs")

const raw = fs.readFileSync("exercises/week-01/raw-leads.json","utf-8")

const leads = JSON.parse(raw)

const validleads = leads.filter(l => l.name.trim() && l.email.trim())

const activeHighScore = validleads.filter(l => l.status === "active" && l.score >= 50)

const transformed = activeHighScore.map(({name,email,company,score}) => ({
    name:name,
    email:email.trim().toLowerCase(),
    company:company,
    score:score
}))

function summarizeLead(transformed){
    const result = {
        totalLeads: 0,
        averageScore: 0,
        companyCounts: {},
        topLead: ""
    }
    result.totalLeads = transformed.length
    const totalScore = transformed.reduce((acc,l) => {
        return acc = acc + l.score
    },0)
    result.companyCounts = transformed.reduce((acc,l) => {
        acc[l.company] = (acc[l.company] || 0) +1 //这里是我看了drill之后改对的，本来用的是result.companyCounts[l.company]
        return acc
    },{})
    result.topLead = transformed.reduce((acc,l) => {
        return acc.score > l.score? acc:l
    }).name
    result.averageScore = Math.round(totalScore / result.totalLeads)
    return result
}
const summary = summarizeLead(transformed)
fs.writeFileSync("exercises/week-01/lead-output.json", JSON.stringify({leads:transformed, summary:summary}, null, 2)) //


console.log(summarizeLead(transformed))