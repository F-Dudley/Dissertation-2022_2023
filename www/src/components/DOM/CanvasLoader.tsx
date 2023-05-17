import { type FC } from 'react';
import { Html, useProgress } from '@react-three/drei';

const CanvasLoader: FC = () => {
	const { progress } = useProgress();

	return (
		<Html center>
			<span>{progress} % Loaded</span>
		</Html>
	);
};

export default CanvasLoader;
