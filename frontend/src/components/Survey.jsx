import Question from './Question'
import { useState } from 'react'

const Survey = ({ questions = [] }) => {
  const [answers, setAnswers] = useState([])
  return (
    <div className=' border border-black flex flex-col justify-center items-center overflow-y-scroll p-5'>
      {questions.map((question, index) => (
        <Question
          key={index}
          question={question.question}
          options={question.options}
          setAnswer={(answer) => setAnswers([...answers, { [index]: answer }])}
        />
      ))}
    </div>
  )
}

export default Survey
