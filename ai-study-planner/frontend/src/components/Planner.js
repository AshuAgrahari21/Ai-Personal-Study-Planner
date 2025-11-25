import React, {useState} from 'react'
import axios from 'axios'
import TaskCard from './TaskCard'


export default function Planner({sample}){
const [plan, setPlan] = useState(null)
const [user, setUser] = useState(sample)


function generate(){
axios.post('http://localhost:5000/api/generate', user)
.then(r => setPlan(r.data.plan))
.catch(e => console.error(e))
}


return (
<div>
<div className="controls">
<button onClick={generate}>Generate Plan</button>
</div>


{plan && (
<div className="plan">
{plan.map(day=> (
<div key={day.day} className="day-card">
<h3>Day {day.day}</h3>
{day.slots.map((s,i)=>(
<TaskCard key={i} task={s} />
))}
</div>
))}
</div>
)}
</div>
)
}