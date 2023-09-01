import { useState } from 'react'


function App() {

  return (
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
        <button type="submit" class="btn">Login</button>
    </form>
</div>
     
  )
}

export default App
