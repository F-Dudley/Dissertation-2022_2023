import { Suspense, useRef } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { Float, Points } from '@react-three/drei';

import PCDViewer from '@/components/canvas/PCDViewer';
import { IsAScanntingTechnique } from '@/data/validation';
import CanvasLoader from '@/components/DOM/CanvasLoader';

const SkullTechniqueID = () => {
	const { techniqueID } = useParams();

	const navigator = useNavigate();
	if (techniqueID === undefined || !IsAScanntingTechnique(techniqueID)) {
		console.log('invalid');
		navigator('/404');
	}

	const cloudRef = useRef<typeof Points>(null);
	const cloudDir = `/clouds/${techniqueID}/Skull.ply`;

	return (
		<Float floatIntensity={0.5} rotationIntensity={1}>
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
