import { Button, Image, Tabs, Upload } from 'antd'
import './App.css'
import Survey from './components/Survey'
import { questions } from './content/diagnoseMeQuestions'
import surveys from './content/surveys'
import { sendSurvey } from './services/api'
import createNotification from './utils/notification'
import ChatBot from './components/ChatBot'
import tips from './content/tips'
import { UploadOutlined } from '@ant-design/icons'

function App() {
  const handleSubmit = async (answers) => {
    try {
      let res = await sendSurvey(answers)
      if (res.status === 200) {
        createNotification(
          'info',
          'Analysis Complete',
          `After meticulous analysis,
          we have come to the conclusion that you are suffering from  ${res.data?.prediction[0]}`
        )
      }
    } catch (error) {
      createNotification('error', 'Error', `something went wrong...`)
    }
  }

  const generateTip = () => {
    let tip = tips[Math.floor(Math.random() * tips.length)]
    createNotification('info', 'Tip', tip)
  }

  return (
    <div className=' grid grid-cols-2 w-full h-screen p-12'>
      <Tabs
        tabBarStyle={{ marginBottom: 0 }}
        defaultActiveKey='1'
        items={surveys.map((survey, index) => ({
          ...survey,
          children: (
            <Survey questions={questions} key={index} onSubmit={handleSubmit} />
          ),
        }))}
      />
      <div className='w-full h-full flex flex-col items-center justify-between'>
        <Image
          src={require('./assets/logo.png')}
          alt='logo'
          width={400}
          preview={false}
        />
        <ChatBot />
        <Button
          type='primary'
          shape='round'
          ghost
          style={{
            backgroundColor: 'lightBlue',
            color: 'black',
            width: '400px',
            margin: '5px',
          }}
          onClick={generateTip}
        >
          Get a Tip
        </Button>
        <Upload
          name='file'
          action={`${process.env.REACT_APP_BASE_URL}/upload/`}
          multiple={false}
          onChange={(info) => {
            if (info.file.status === 'done' && info.file.response.result)
              createNotification(
                'info',
                'Analysis Complete',
                `After meticulous analysis,
                we have come to the conclusion that you are  ${info.file?.response?.result}`
              )
            else if (info.file.status === 'error')
              createNotification('error', 'Error', `something went wrong...`)
          }}
          showUploadList={false}
        >
          <Button
            icon={<UploadOutlined />}
            type='primary'
            shape='round'
            ghost
            style={{
              backgroundColor: 'lightBlue',
              color: 'black',
              width: '500px',
              margin: '5px',
            }}
          >
            Upload a x-ray image to check whether you have covid or not.
          </Button>
        </Upload>
      </div>
    </div>
  )
}

export default App
