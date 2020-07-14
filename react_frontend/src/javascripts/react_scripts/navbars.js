import React from 'react';
import ReactDOM from 'react-dom';



export class TopNavBar extends React.Component
{
  render()
  {
    return (
      <div>
        <header class="site-header">
          <nav class="navbar navbar-expand-md navbar-dark bg-steel fixed-top">
          <div class="container">
            <a class="navbar-brand mr-4" href="/">Flask Blog</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarToggle" aria-controls="navbarToggle" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarToggle">
              <div class="navbar-nav mr-auto">
                <a class="nav-item nav-link" href="/">Home</a>
                <a class="nav-item nav-link" href="/about">About</a>
              </div>
              <div id="user_profile_section_id"></div>
            </div>
          </div>
          </nav>
        </header>
      </div>
    );
  }
}

export class SideNavBar extends React.Component
{
  render()
  {
    return (
      <div>
        <div class="content-section">
        <h3>Our Sidebar</h3>
        <p class='text-muted'>You can put any information here you'd like.
          <ul class="list-group">
          <li class="list-group-item list-group-item-light">Latest Posts</li>
          <li class="list-group-item list-group-item-light">Announcements</li>
          <li class="list-group-item list-group-item-light">Calendars</li>
          <li class="list-group-item list-group-item-light">etc</li>
          </ul>
        </p>
        </div>
      </div>
    );
  }
}

export class UserProfileSection extends React.Component
{
  render()
  {
    return (
      <div>
        {this.props.is_logged_in ? 
        (
          <div class="navbar-nav">
            <a class="nav-item nav-link" href="/account">Account</a>
            <a class="nav-item nav-link" href="/logout">Log out</a>
          </div>
        ) : 
        ( 
          <div class="navbar-nav">
            <a class="nav-item nav-link" href="/login">Login</a>
            <a class="nav-item nav-link" href="/register">Register</a>
          </div>
        )}
      </div>
    );
  }
}

var top_navbar_div = document.getElementById("top_navbar_id");
var side_navbar_div = document.getElementById("side_navbar_id");
var is_logged_in_str = top_navbar_div.getAttribute("is_logged_in");
var is_logged_in = (is_logged_in_str === 'True');


if(top_navbar_div)
{
  ReactDOM.render(<TopNavBar />, top_navbar_div);
  ReactDOM.render(<UserProfileSection is_logged_in={is_logged_in} />, document.getElementById("user_profile_section_id"))
}

if(side_navbar_div) ReactDOM.render(<SideNavBar />, side_navbar_div);






