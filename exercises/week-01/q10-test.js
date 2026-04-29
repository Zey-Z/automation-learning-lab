const apiData = '{"results":[{"employee_id":"E-001","full_name":"Alice Chen","dept":"ENG","compensation":{"base":95000,"bonus":8000}},{"employee_id":"E-002","full_name":"Bob Kim","dept":"SALES","compensation":{"base":72000}},{"employee_id":"E-003","full_name":"Carol Park","dept":"ENG","compensation":{"base":110000,"bonus":15000}}]}';

function normalizeEmployees(apiData){
  const parsed = JSON.parse(apiData)
  const result = parsed.results.map(({employee_id,full_name,dept,compensation: {base,bonus=0}}) => ({
    id:employee_id,
    name:full_name,
    department:dept,
    totalPay:base+bonus
  })).filter(e=> e.totalPay > 100000)
  return result
}

console.log(normalizeEmployees(apiData));
