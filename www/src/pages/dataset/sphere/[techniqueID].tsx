import { Suspense, useRef, useState, useMemo } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { Float, Points } from '@react-three/drei';

import PCDViewer from '@/components/canvas/PCDViewer';
import { IsAScanntingTechnique } from '@/data/validation';
import CanvasLoader from '@/components/DOM/CanvasLoader';
import { DistMaps } from '@/data/assets';
import Root from '@/components/tunnels/Root';

const SphereTechniqueID = () => {
	const { techniqueID } = useParams();

	const navigator = useNavigate();
	if (techniqueID === undefined || !IsAScanntingTechnique(techniqueID)) {
		console.log('invalid');
		navigator('/404');
	}

	const cloudRef = useRef<typeof Points>(null);
	const [showDistMap, setShowDistMap] = useState<boolean>(true);

	const cloudDir = `/clouds/${techniqueID}/Sphere.ply`;
	const distMapCols = useMemo<Float32Array>(
		() => new Float32Array(DistMaps.get(techniqueID)),
		[techniqueID],
	);

	return (
		<Float floatIntensity={0.5} rotationIntensity={1}>
			<Suspense fallback={<CanvasLoader />}>
				<PCDViewer
					ref={cloudRef}
					dir={cloudDir}
					loading={<CanvasLoader />}
					customColors={showDistMap ? distMapCols : undefined}
				/>
			</Suspense>
		</Float>
	);
};

export default SphereTechniqueID;
