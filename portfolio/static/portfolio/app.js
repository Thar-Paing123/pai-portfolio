const menuButton = document.querySelector('.menu-button');
const navigation = document.querySelector('#navigation');
menuButton.addEventListener('click', () => {
  const open = menuButton.getAttribute('aria-expanded') !== 'true';
  menuButton.setAttribute('aria-expanded', String(open));
  menuButton.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
  navigation.classList.toggle('open', open);
});
navigation.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
  navigation.classList.remove('open');
  menuButton.setAttribute('aria-expanded', 'false');
  menuButton.setAttribute('aria-label', 'Open navigation');
}));
const projectCards = [...document.querySelectorAll('.project-card')];
const searchInput = document.querySelector('#project-search');
const loadMore = document.querySelector('#load-more');
const resultStatus = document.querySelector('#filter-status');
const pageSize = 9;
let selectedCategory = 'all';
let visibleLimit = pageSize;
function updateProjects() {
  const query = searchInput.value.trim().toLowerCase();
  const matches = projectCards.filter(card =>
    (selectedCategory === 'all' || card.dataset.category === selectedCategory) &&
    card.textContent.toLowerCase().includes(query));
  const visible = matches.slice(0, visibleLimit);
  projectCards.forEach(card => { card.hidden = !visible.includes(card); });
  resultStatus.textContent = `Showing ${visible.length} of ${matches.length} projects`;
  document.querySelector('#project-empty').hidden = matches.length !== 0;
  loadMore.hidden = matches.length <= visibleLimit;
  if (!loadMore.hidden) loadMore.innerHTML = `Show more projects <span aria-hidden="true">↓</span>`;
}
function setCategory(category) {
  selectedCategory = category;
  visibleLimit = pageSize;
  document.querySelectorAll('.filter').forEach(button => {
    const active = button.dataset.filter === category;
    button.classList.toggle('active', active);
    button.setAttribute('aria-pressed', String(active));
  });
  updateProjects();
}
document.querySelectorAll('.filter').forEach(button => button.addEventListener('click', () => setCategory(button.dataset.filter)));
searchInput.addEventListener('input', () => { visibleLimit = pageSize; updateProjects(); });
loadMore.addEventListener('click', () => {
  const previousLimit = visibleLimit;
  visibleLimit += pageSize;
  updateProjects();
  const newlyVisible = projectCards.filter(card => !card.hidden)[previousLimit];
  if (newlyVisible) newlyVisible.querySelector('summary').focus({preventScroll:true});
});
document.querySelector('#clear-search').addEventListener('click', () => {
  searchInput.value = '';
  setCategory('all');
  searchInput.focus();
});
updateProjects();
document.addEventListener('keydown', event => {
  if (event.key === 'Escape') {
    navigation.classList.remove('open');
    menuButton.setAttribute('aria-expanded', 'false');
    menuButton.setAttribute('aria-label', 'Open navigation');
  }
});
document.querySelector('#copy-email').addEventListener('click', async () => {
  const status = document.querySelector('#copy-status');
  try {
    await navigator.clipboard.writeText('paingphyothet561@gmail.com');
    status.textContent = 'Email address copied.';
  } catch {
    status.textContent = 'Please copy the email address above or click it to open your email app.';
  }
});
const links = [...navigation.querySelectorAll('a')];
const sections = links.map(link => document.querySelector(link.getAttribute('href')));
if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) links.forEach(link => {
        const active = link.getAttribute('href') === `#${entry.target.id}`;
        link.classList.toggle('active', active);
        if (active) link.setAttribute('aria-current', 'location');
        else link.removeAttribute('aria-current');
      });
    });
  }, { rootMargin: '-15% 0px -55% 0px' });
  sections.forEach(section => observer.observe(section));
}
