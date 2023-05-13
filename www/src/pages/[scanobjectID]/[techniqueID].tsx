import { Suspense, useRef } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { Float, Points } from '@react-three/drei';

import PCDViewer from '@/components/canvas/PCDViewer';
import { SCANNING_TECHNIQUES, SCANNING_OBJECTS } from '@/data/constants';
import CanvasLoader from '@/components/DOM/CanvasLoader';
import ReturnBar from '@/layout/ReturnBar';

const SkullTechniqueID = () => {
	const { scanobjectID, techniqueID } = useParams();

	const navigator = useNavigate();
	if (
		scanobjectID === undefined ||
		techniqueID === undefined ||
		!SCANNING_OBJECTS.includes(scanobjectID) ||
		!SCANNING_TECHNIQUES.includes(techniqueID)
	) {
		console.log('invalid');
		navigator('/404');
	}

	const cloudRef = useRef<typeof Points>(null);
	const cloudDir = `/clouds/${techniqueID}/${scanobjectID}.ply`;

	return (
		<Float floatIntensity={0.5} rotationIntensity={1}>
			<ReturnBar />
			<Suspense fallback={<CanvasLoader />}>
				<PCDViewer
					ref={cloudRef}
					dir={cloudDir}
					loading={<CanvasLoader />}
				/>
			</Suspense>
		</Float>
	);
};

export default SkullTechniqueID;
