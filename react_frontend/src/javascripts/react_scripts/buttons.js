import React from 'react';
import ReactDOM from 'react-dom';
//import * as serviceWorker from './serviceWorker';

function attachActive(new_active_button, old_active_button)
{
    new_active_button.classList.add("active");
    old_active_button.classList.remove("active");
}

window.onload = function () {
    var reveal_button = document.getElementById("reveal_button_id");
    var anonymous_button = document.getElementById("anonymous_button_id");
    var top_navbar_div = document.getElementById("top_navbar_id");
    var is_anonymous = top_navbar_div.getAttribute("is_anonymous") === "True";
    var current_user_username = top_navbar_div.getAttribute("current_user_username");

    if (reveal_button) reveal_button.onclick = function() { attachActive(reveal_button, anonymous_button); }; 
    if (anonymous_button) anonymous_button.onclick = function() { attachActive(anonymous_button, reveal_button); };
    is_anonymous ? attachActive(anonymous_button, reveal_button) : attachActive(reveal_button, anonymous_button);
    
    if (current_user_username == "Guest")
    {
        reveal_button.classList.remove("active");
        anonymous_button.classList.remove("active");
        reveal_button.classList.add("disabled");
        anonymous_button.classList.add("disabled");
        document.getElementById("identity_intro_id").innerHTML = "Please log in to select identity.";
    }
    
};



// class BlogPosts extends React.Component
// {
//   render()
//   {
    
//   }
// }

// var blog_posts_div = document.getElementById("blog_posts_id");
// if(blog_posts_div)
// {
//   var posts = {...(blog_posts_div.dataset)};
//   ReactDOM.render(<BlogPosts posts={posts} />, blog_posts_div);
// }





// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
//serviceWorker.unregister();