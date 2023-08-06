import axios from 'axios'

const BE = axios.create({
  baseURL: process.env.REACT_APP_BASE_URL,
})

const sendSurvey = async (survey) => await BE.post('/survey/', survey)
const askChatbot = async (question) => await BE.post('/chat_bot/', question)

export { sendSurvey, askChatbot }
