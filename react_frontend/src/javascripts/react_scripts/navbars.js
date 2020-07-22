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
            <a class="navbar-brand mr-4" href="/">Annony Blog</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarToggle" aria-controls="navbarToggle" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarToggle">
              <div class="navbar-nav mr-auto">
                <a class="nav-item nav-link" href="/post/new">New post</a>
                {this.props.logged_in_username != "Guest" && this.props.logged_in_username != '' && 
                (
                  <div class="navbar-nav">
                    <a class="nav-item nav-link" href={"/user/" + this.props.logged_in_username}>My posts</a>
                  </div>
                )}
              </div>
              {this.props.logged_in_username != "Guest" && this.props.logged_in_username != '' ? 
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

var top_navbar_div = document.getElementById("top_navbar_id");
var side_navbar_div = document.getElementById("side_navbar_id");
var logged_in_username = top_navbar_div.getAttribute("logged_in_username");

console.log("DEBUG: logged_in_username type:", typeof(logged_in_username),", data: -", logged_in_username, '-')

if(top_navbar_div)
{
  ReactDOM.render(<TopNavBar logged_in_username={logged_in_username} />, top_navbar_div);
}

if(side_navbar_div) ReactDOM.render(<SideNavBar />, side_navbar_div);






