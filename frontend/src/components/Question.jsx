import { Radio } from 'antd'

const Question = ({
  question = '',
  options = [],
  setAnswer = () => null,
  label = '',
}) => {
  return (
    <div className='h-full w-full'>
      <h1 className=' font-bold text-xl'>
        <span>{label}. </span>
        {question}
      </h1>
      <Radio.Group
        style={{ padding: '5px' }}
        onChange={(e) => setAnswer(e.target.value)}
      >
        {options.map((option, index) => (
          <Radio key={index} value={option} style={{ padding: '5px' }}>
            {option}
          </Radio>
        ))}
      </Radio.Group>
    </div>
  )
}

export default Question
