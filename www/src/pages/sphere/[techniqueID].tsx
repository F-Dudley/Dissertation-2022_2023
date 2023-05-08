import { type FC, useRef } from 'react';
import { useParams } from 'react-router-dom';
import PCDViewer from '@/components/canvas/PCDViewer';
import Root from '@/components/tunnels/Root';
import { SCANNING_TECHNIQUES } from '@/data/constants';
import CanvasLoader from '@/components/DOM/CanvasLoader';
import { Float, Points } from '@react-three/drei';
import ReturnBar from '@/layout/ReturnBar';

const SphereTechniqueID: FC = () => {
	const { techniqueID } = useParams();

	const cloudRef = useRef<typeof Points>(null);

	if (!SCANNING_TECHNIQUES.includes(techniqueID as string) || !techniqueID) {
		console.log(`TechniqueID: ${techniqueID} is not a valid technique ID.`);
		return (
			<Root.In>
				<h1>404</h1>
			</Root.In>
		);
	}

	const cloudDir = `/clouds/${techniqueID}/sphere.ply`;

	return (
		<Float floatIntensity={0.5} rotationIntensity={1}>
			<ReturnBar />
			<PCDViewer
				// eslint-disable-next-line @typescript-eslint/ban-ts-comment
				// @ts-ignore
				ref={cloudRef}
				dir={cloudDir}
				loading={<CanvasLoader />}
			/>
		</Float>
	);
};

export default SphereTechniqueID;
