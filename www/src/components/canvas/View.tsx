import type { FC, PropsWithChildren } from 'react'
import R3F from '../tunnels/R3F'

const View : FC<PropsWithChildren> = ({ children }) => {
  return (
    <R3F.In>
        {children}
    </R3F.In>
  )
}

export default View