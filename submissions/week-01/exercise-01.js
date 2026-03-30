const leads = [
  { name: "  Alice ", email: "  ALICE@EXAMPLE.COM ", source: "webinar" },
  { name: "Bob", email: "", source: "referral" },
  { name: " Charlie", email: "charlie@test.com  ", source: "ads" },
  { name: "", email: "dave@example.com", source: "webinar" },
  { name: "Eve", email: "   EVE@SAMPLE.COM", source: "" },
  { name: " Frank ", email: "frank@test.com", source: "referral" },
];

function cleanLeads(leads){
  const result ={
    cleaned : [],
    rejected : []
  }

  result.cleaned = leads.filter(lead => lead.name.trim() && lead.email.trim())
  result.rejected = leads.filter(lead => !lead.name.trim() || !lead.email.trim())
  result.cleaned = result.cleaned.map(lead => {
    return {
      name: lead.name.trim(),
      email : lead.email.trim().toLowerCase(),
      source : lead.source
    }
  })
  return result
}


console.log(cleanLeads(leads))