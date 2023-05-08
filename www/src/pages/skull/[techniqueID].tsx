import { useRef } from 'react';
import { useParams } from 'react-router-dom';
import { Float, Html, Points } from '@react-three/drei';

import PCDViewer from '@/components/canvas/PCDViewer';
import { SCANNING_TECHNIQUES } from '@/data/constants';
import CanvasLoader from '@/components/DOM/CanvasLoader';
import ReturnBar from '@/layout/ReturnBar';

const SkullTechniqueID = () => {
	const { techniqueID } = useParams();

	const cloudRef = useRef<typeof Points>(null);

	if (!SCANNING_TECHNIQUES.includes(techniqueID as string) || !techniqueID) {
		console.log(`TechniqueID: ${techniqueID} is not a valid technique ID.`);
		return (
			<Html center>
				<h1>404</h1>
			</Html>
		);
	}

	const cloudDir = `/clouds/${techniqueID}/skull.ply`;

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

export default SkullTechniqueID;
