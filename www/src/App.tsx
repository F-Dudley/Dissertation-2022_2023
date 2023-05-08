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
			<div className="w-full h-full bg-slate-800 text-white">
				<Root.Out />
				<Canvas
					className="absolute top-0 left-0 w-screen min-h-screen -z-5"
					camera={{ near: 0.001 }}
					style={{ background: '#000000' }}
				>
					{useRoutes(routes)}
					<R3F.Out />
					<OrbitControls />
					<Stage />
				</Canvas>
			</div>
		</>
	);
}

export default App;
