import './App.css'
import Survey from './components/Survey'
import { questions } from './content/diagnoseMeQuestions'

function App() {
  return (
    <div className=' grid grid-cols-2 w-full h-screen p-20'>
      <Survey questions={questions} />
    </div>
  )
}

export default App
