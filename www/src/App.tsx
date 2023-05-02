import { useRoutes } from 'react-router-dom'
import { Canvas } from '@react-three/fiber'
import { OrbitControls } from '@react-three/drei'

// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-ignore
import routes from '~react-pages'

import R3F from '@/components/tunnels/R3F'
import Root from '@/components/tunnels/Root'

function App() {

  return (
    <div className='w-full h-full bg-slate-800 text-white'>
      <div className='absolute top-0 left-0 w-screen min-h-screen'>
        <Root.Out />
      </div>
      {useRoutes(routes)}
      <Canvas className='absolute top-0 left-0 w-screen min-h-screen' camera={{ near: 0.001 }}>
        <R3F.Out />
        <OrbitControls />
        <gridHelper />
      </Canvas>
    </div>
  )
}

export default App
