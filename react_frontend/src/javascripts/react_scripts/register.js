import React from 'react';
import ReactDOM from 'react-dom';
//import * as serviceWorker from './serviceWorker';

class Register extends React.Component
{
  render()
  {
    return (
      <div>
        <div class="content-section">
          <form method="POST" action="">
            {form.hidden_tag}
            <legend class="border-bottom mb-4">Join Today</legend>

            <div class="form-group">
              <div class="form-control-label">{form.username.label}</div>
              <div class="form-control form-control-lg">{form.username}</div>
            </div>

            <div class="form-group">
              <div class="form-control-label">{form.email.label}</div>
              <div class="form-control form-control-lg">{form.email}</div>
            </div>

            <div class="form-group">
              <div class="form-control-label">{form.password.label}</div>
              <div class="form-control form-control-lg">{form.password}</div>
            </div>

            <div class="form-group">
              <div class="form-control-label">{form.confirm_password.label}</div>
              <div class="form-control form-control-lg">{form.confirm_password}</div>
            </div>

            <div class="form-group">
              <div class="btn btn-outline-info">{form.submit}</div>
            </div>

          </form>
        </div>
        <div class="border-top pt-3">
          <small class="text-muted">
            Already have an account? <a class="ml-2" href="{ url_for('login') }">Sign In</a>
          </small>
        </div>
      </div>

    );
  }
}

var register_div = document.getElementById("register_div_id");
if (register_div)
{
  // var input_form = {...(register_div.dataset)};
  // console.log("input_form currently is: ", input_form)
  ReactDOM.render(<Register />, register_div);
}

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
//serviceWorker.unregister();
