async function loadEvents() {
    const res = await fetch('/events');
    const data = await res.json();
  
    const feed = document.getElementById('feed');
    feed.innerHTML = '';
  
    data.reverse().forEach(event => {
      let line = '';
      const date = new Date(event.timestamp).toUTCString();
  
      if (event.event_type === 'push') {
        line = `${event.author} pushed to ${event.to_branch} on ${date}`;
      } else if (event.event_type === 'pull_request') {
        line = `${event.author} submitted a pull request from ${event.from_branch} to ${event.to_branch} on ${date}`;
      } else if (event.event_type === 'merge') {
        line = `${event.author} merged branch ${event.from_branch} to ${event.to_branch} on ${date}`;
      }
  
      const div = document.createElement('div');
      div.className = 'event';
      div.textContent = line;
      feed.appendChild(div);
    });
  }
  
  loadEvents();
  setInterval(loadEvents, 15000);
  