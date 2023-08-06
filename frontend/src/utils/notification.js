import { notification } from 'antd'

const createNotification = (type, message, description) =>
  notification.open({
    message,
    description,
    type,
  })

export default createNotification
