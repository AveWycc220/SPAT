if (document.documentElement.clientWidth <= 1024) {
  document.querySelector('.header_text').textContent = "Your device doesn't support"
}

const firstDiv = document.querySelector('.first')
const secondDiv = document.querySelector('.second')
const thirdDiv = document.querySelector('.third')
const firstPlot = document.querySelector('.first-plot')
const secondPlot = document.querySelector('.second-plot')
const thirdPlot = document.querySelector('.third-plot')
const firstPlotImg = document.querySelector('.plot1-img')
const secondPlotImg = document.querySelector('.plot2-img')
const thirdPlotImg = document.querySelector('.plot3-img')
const firstButton = document.querySelector('#image-button-1')
const secondButton = document.querySelector('#image-button-2')
const thirdButton = document.querySelector('#image-button-3')
const firstPlotInter = document.querySelector('.plot1')
const secondPlotInter = document.querySelector('.plot2')
const thirdPlotInter = document.querySelector('.plot3')
const input = document.querySelector('.n-input')

firstPlot.style.display = 'none'
secondPlot.style.display = 'none'
thirdPlot.style.display = 'none'
firstPlotImg.style.display = 'none'
secondPlotImg.style.display = 'none'
thirdPlotImg.style.display = 'none'
firstButton.style.display = 'none'
secondButton.style.display = 'none'
thirdButton.style.display = 'none'

firstDiv.addEventListener('click', () => {
  if (secondPlot.style.display === 'none' && thirdPlot.style.display === 'none' && firstPlot.style.display !== 'block') {
    firstPlot.style.display = 'block'
    firstButton.style.display = 'block'
    firstDiv.classList.remove('active')
    secondDiv.classList.remove('active')
    thirdDiv.classList.remove('active')
    secondDiv.style.opacity = '50%'
    thirdDiv.style.opacity = '50%'
  } else if (firstPlot.style.display === 'block') {
    firstPlot.style.display = 'none'
    firstDiv.classList.add('active')
    secondDiv.classList.add('active')
    thirdDiv.classList.add('active')
    secondDiv.style.opacity = '100%'
    thirdDiv.style.opacity = '100%'
  }
  console.log('First div clicked')
})

secondDiv.addEventListener('click', () => {
  if (firstPlot.style.display === 'none' && thirdPlot.style.display === 'none' && secondPlot.style.display !== 'block') {
    secondPlot.style.display = 'block'
    secondButton.style.display = 'block'
    firstDiv.classList.remove('active')
    secondDiv.classList.remove('active')
    thirdDiv.classList.remove('active')
    firstDiv.style.opacity = '50%'
    thirdDiv.style.opacity = '50%'
  } else if (secondPlot.style.display === 'block') {
    secondPlot.style.display = 'none'
    firstDiv.classList.add('active')
    secondDiv.classList.add('active')
    thirdDiv.classList.add('active')
    firstDiv.style.opacity = '100%'
    thirdDiv.style.opacity = '100%'
  }
  console.log('Second div clicked')
})

thirdDiv.addEventListener('click', () => {
  if (firstPlot.style.display === 'none' && secondPlot.style.display === 'none' && thirdPlot.style.display !== 'block') {
    thirdPlot.style.display = 'block'
    thirdButton.style.display = 'block'
    firstDiv.classList.remove('active')
    secondDiv.classList.remove('active')
    thirdDiv.classList.remove('active')
    secondDiv.style.opacity = '50%'
    firstDiv.style.opacity = '50%'
  } else if (thirdPlot.style.display === 'block') {
    thirdPlot.style.display = 'none'
    firstDiv.classList.add('active')
    secondDiv.classList.add('active')
    thirdDiv.classList.add('active')
    secondDiv.style.opacity = '100%'
    firstDiv.style.opacity = '100%'
  }
  console.log('Third div clicked')
})

firstButton.addEventListener('click', () => {
  if (firstPlotImg.style.display === 'none') {
    firstPlotImg.style.display = 'block'
    firstPlotInter.style.display = 'none'
    firstButton.textContent = 'Interactive'
  } else if (firstPlotImg.style.display === 'block') {
    firstPlotImg.style.display = 'none'
    firstPlotInter.style.display = 'block'
    firstButton.textContent = 'Image'
  }
})

secondButton.addEventListener('click', () => {
  if (secondPlotImg.style.display === 'none') {
    secondPlotImg.style.display = 'block'
    secondPlotInter.style.display = 'none'
    secondButton.textContent = 'Interactive'
  } else if (secondPlotImg.style.display === 'block') {
    secondPlotImg.style.display = 'none'
    secondPlotInter.style.display = 'block'
    secondButton.textContent = 'Image'
  }
})

thirdButton.addEventListener('click', () => {
  if (thirdPlotImg.style.display === 'none') {
    thirdPlotImg.style.display = 'block'
    thirdPlotInter.style.display = 'none'
    thirdButton.textContent = 'Interactive'
  } else if (thirdPlotImg.style.display === 'block') {
    thirdPlotImg.style.display = 'none'
    thirdPlotInter.style.display = 'block'
    thirdButton.textContent = 'Image'
  }
})

input.onclick = () => {
  input.value = 'Press Enter after input'
  input.select()
}

input.addEventListener('keydown', (e) => {
  if (e.keyCode === 13) {
    document.location.href += input.value
  }
})
