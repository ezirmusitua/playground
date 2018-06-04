import './main.scss'
import 'github-markdown-css/github-markdown.css'
import {Resource} from './resource'
import MarkdownIt from 'markdown-it'
import {GlobalLogger} from './logger'


window.renderMD = () => {
  const markdown = MarkdownIt()
  const markdownRaw = markdown.render(Resource.md)
  const body = document.getElementById('app')
  const mdContainer = document.createElement('div')
  mdContainer.setAttribute('class', 'markdown-body')
  mdContainer.setAttribute('id', 'content')
  mdContainer.innerHTML = markdownRaw
  body.appendChild(mdContainer)
  GlobalLogger.info('Markdown Content Appended!')
}


