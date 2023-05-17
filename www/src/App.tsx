import { useRoutes } from 'react-router-dom';
import { Canvas } from '@react-three/fiber';
import { OrbitControls, Stage } from '@react-three/drei';

// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-ignore
import routes from '~react-pages';

import R3F from '@/components/tunnels/R3F';
import Root from './components/tunnels/Root';

function App() {
	return (
		<>
			<div className="z-10">
				<Root.Out />
			</div>
			<Canvas
				className="absolute top-0 left-0 w-full min-h-screen -z-1"
				camera={{ near: 0.001 }}
			>
				{useRoutes(routes)}
				<R3F.Out />
				<OrbitControls />
				<Stage />
			</Canvas>
		</>
	);
}

export default App;
