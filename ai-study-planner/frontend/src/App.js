import React, {useEffect, useState} from 'react'
import axios from 'axios'
import Planner from './components/Planner'


export default function App(){
const [sample, setSample] = useState(null)


useEffect(()=>{
axios.get('http://localhost:5000/api/sample')
.then(r => setSample(r.data))
.catch(e => console.error(e))
},[])


return (
<div className="app">
<header>
<h1>AI Personal Study Planner</h1>
<p>Adaptive timetable generated using priority scheduling</p>
</header>
<main>
{sample ? <Planner sample={sample} /> : <p>Loading...</p>}
</main>
</div>
)
}