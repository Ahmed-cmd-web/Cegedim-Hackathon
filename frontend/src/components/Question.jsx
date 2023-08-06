import { Radio } from 'antd'

const Question = ({ question = '', options = [], setAnswer = () => null }) => {
  return (
    <div className='h-full w-full'>
      <h1 className=' font-bold'>{question}</h1>
      <Radio.Group onChange={(e) => setAnswer(e.target.value)}>
        {options.map((option, index) => (
          <Radio key={index} value={option}>
            {option}
          </Radio>
        ))}
      </Radio.Group>
    </div>
  )
}

export default Question
