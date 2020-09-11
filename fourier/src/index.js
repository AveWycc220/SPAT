if (document.documentElement.clientWidth <= 1024) {
  document.querySelector('.header_text').textContent = "Your device doesn't support"
}

const firstDiv = document.querySelector('.first')
const secondDiv = document.querySelector('.second')
const thirdDiv = document.querySelector('.third')
const firstPlot = document.querySelector('.first-plot')
const secondPlot = document.querySelector('.second-plot')
const thirdPlot = document.querySelector('.third-plot')

firstPlot.style.display = 'none'
secondPlot.style.display = 'none'
thirdPlot.style.display = 'none'

firstDiv.addEventListener('click', () => {
  if (secondPlot.style.display === 'none' && thirdPlot.style.display === 'none' && firstPlot.style.display !== 'block') {
    firstPlot.style.display = 'block'
    firstDiv.classList.remove('active')
    secondDiv.classList.remove('active')
    thirdDiv.classList.remove('active')
  } else if (firstPlot.style.display === 'block') {
    firstPlot.style.display = 'none'
    firstDiv.classList.add('active')
    secondDiv.classList.add('active')
    thirdDiv.classList.add('active')
  }
  console.log('First div clicked')
})

secondDiv.addEventListener('click', () => {
  if (firstPlot.style.display === 'none' && thirdPlot.style.display === 'none' && secondPlot.style.display !== 'block') {
    secondPlot.style.display = 'block'
    firstDiv.classList.remove('active')
    secondDiv.classList.remove('active')
    thirdDiv.classList.remove('active')
  } else if (secondPlot.style.display === 'block') {
    secondPlot.style.display = 'none'
    firstDiv.classList.add('active')
    secondDiv.classList.add('active')
    thirdDiv.classList.add('active')
  }
  console.log('Second div clicked')
})

thirdDiv.addEventListener('click', () => {
  if (firstPlot.style.display === 'none' && secondPlot.style.display === 'none' && thirdPlot.style.display !== 'block') {
    thirdPlot.style.display = 'block'
    firstDiv.classList.remove('active')
    secondDiv.classList.remove('active')
    thirdDiv.classList.remove('active')
  } else if (thirdPlot.style.display === 'block') {
    thirdPlot.style.display = 'none'
    firstDiv.classList.add('active')
    secondDiv.classList.add('active')
    thirdDiv.classList.add('active')
  }
  console.log('Third div clicked')
})
