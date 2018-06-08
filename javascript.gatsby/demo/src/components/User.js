import React, {Component} from 'react'
import styles from './User.module.scss'

export default class User extends Component {
  constructor() {
    super()
  }

  render() {
    const props = this.props
    return (
      <div className={styles.user}>
        <img src={props.avatar} className={styles.avatar} alt=""/>
        <div className={styles.description}>
          <h2 className={styles.username}>
            {props.username}
          </h2>
          <p className={styles.excerpt}>
            {props.excerpt}
          </p>
        </div>
      </div>
    )
  }
}