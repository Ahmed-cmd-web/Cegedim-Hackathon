import { Button } from 'antd'
import Question from './Question'
import { useState } from 'react'

const Survey = ({ questions = [], onSubmit = () => null }) => {
  const [answers, setAnswers] = useState({})
  return (
    <div className=' border border-black flex flex-col h-[40rem] overflow-scroll p-16  bg-white  '>
      {questions.map((question, index) => (
        <Question
          key={index}
          question={question.question}
          options={question.options}
          label={index + 1}
          setAnswer={(answer) =>
            setAnswers({ ...answers, ...{ [index + 1]: answer } })
          }
        />
      ))}
      <Button
        type='primary'
        onClick={() => {
          let finalAnswers = []
          Object.keys(answers).forEach((key) => {
            finalAnswers.push({ question: key, answer: answers[key] })
          })
          onSubmit(finalAnswers)
        }}
        shape='round'
        block
        ghost
      >
        Submit
      </Button>
    </div>
  )
}

export default Survey
