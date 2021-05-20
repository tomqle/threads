import React, { Component } from "react";
import axiosInstance from "../axiosApi";

class Login extends Component {
  constructor(props) {
    super(props);
    this.state = { username: "", password: "" };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({ [event.target.name]: event.target.value });
  }

  async handleSubmit(event) {
    event.preventDefault();

    try {

      const response = await axiosInstance.post('/token/obtain/', {
        username: this.state.username,
        password: this.state.password
      });

      console.log("response: ", JSON.stringify(response, null, 4));

      axiosInstance.defaults.headers['Authorization'] = 'JWT ' + response.data.access;
      localStorage.setItem('access_token', response.data.access);
      localStorage.setItem('refresh_token', response.data.refresh);
      console.log("access: ", JSON.stringify(response.data.access, null, 4));
      console.log("refresh: ", JSON.stringify(response.data.refresh, null, 4));

      return response;

    } catch (error) {
      throw error;
    }
  }

  render() {
    return(
      <div>login
        <form onSubmit={this.handleSubmit}>
          <label>
            username:
            <input name="username" type="text" value={ this.state.username } onChange={ this.handleChange } />
          </label>
          <label>
            password:
            <input name="password" type="password" value={ this.state.password } onChange={ this.handleChange } />
          </label>
          <input type="submit" value="submit" />
        </form>
      </div>
    )
  }
}

export default Login;