import React from 'react'


export default function TaskCard({task}){
return (
<div className="task-card">
<div className="left">
<strong>{task.subject}</strong>
<div>{task.title}</div>
</div>
<div className="right">
<div>{task.hours} hrs</div>
<div>Priority: {task.priority}</div>
</div>
</div>
)
}