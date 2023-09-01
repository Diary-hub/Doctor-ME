import React from 'react'
import '../styles/login.css'
import Index from './Index.jsx';

import {BrowserRouter as Router,Link,Routes,Route}  from 'react-router-dom';




function Login() {

  return (
    <div>

    <Router>
  <div class="wrapper">
  <form action="">
      <h1>DHS</h1>
      <h4>Doctor Helping Services</h4>
      <div class="input-box">
          <input type="text" placeholder="Username" required/>
          <i class='bx bxs-user'></i>
      </div>
      <div class="input-box">
          <input type="password" placeholder="Password" required/>
          <i class='bx bxs-lock-alt' ></i>
      </div>
      
      <button type="submit" class="btn"><Link to='/index'>Login</Link></button>

      <Routes>
        <Route path="/index" element={<Index />} />

      </Routes>

  </form>
</div>
      </Router>
   
  </div>
  )
}

export default Login
