import { Button, Image, Input } from 'antd'
import { useState } from 'react'
import createNotification from '../utils/notification'
import { askChatbot } from '../services/api'
import { LoadingOutlined } from '@ant-design/icons'

const ChatBot = () => {
  const [question, setQuestion] = useState('')
  const [answer, setAnswer] = useState('Am waiting a question from you!')
  const [loading, setLoading] = useState(false)
  const handleSubmit = async (question) => {
    setLoading(true)
    try {
      let res = await askChatbot({ question })
      if (res.status === 200) setAnswer(res.data?.message)
      else createNotification('error', 'Error', 'Something went wrong')
    } catch (error) {
      createNotification('error', 'Error', error.message)
    } finally {
      setLoading(false)
    }
  }
  return (
    <div className='flex flex-col h-full justify-between'>
      <Image src={require('../assets/chatBot.png')} width={400} preview={false} />
      <Input
        placeholder='I have fever,what should I do?'
        onChange={(e) => setQuestion(e.target.value)}
        size='large'
      />
      {loading ? (
        <LoadingOutlined style={{ fontSize: 34, color: 'blue' }} spin />
      ) : (
        <p className=' font-bold text-center text-white text-2xl '>{answer}</p>
      )}
      <Button
        type='primary'
        shape='round'
        ghost
        style={{ backgroundColor: 'lightBlue', color: 'black' }}
        onClick={() => handleSubmit(`${question},What should I do?`)}
      >
        Tell Me
      </Button>
    </div>
  )
}

export default ChatBot
