import { Suspense, useRef } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { Float, Points } from '@react-three/drei';

import PCDViewer from '@/components/canvas/PCDViewer';
import { IsAScanntingTechnique } from '@/data/validation';
import CanvasLoader from '@/components/DOM/CanvasLoader';
import Root from '@/components/tunnels/Root';

const SkullTechniqueID = () => {
	const { techniqueID } = useParams();

	const navigator = useNavigate();
	if (techniqueID === undefined || !IsAScanntingTechnique(techniqueID)) {
		console.log('invalid');
		navigator('/404');
	}

	const cloudRef = useRef<typeof Points | null>(null);
	const cloudDir = `/clouds/${techniqueID}/Skull.ply`;

	return (
		<>
			<Float floatIntensity={0.5} rotationIntensity={1}>
				<Suspense fallback={<CanvasLoader />}>
					<PCDViewer
						ref={cloudRef}
						dir={cloudDir}
						loading={<CanvasLoader />}
					/>
				</Suspense>
			</Float>
			<Root.In>
				<button
					className="absolute top-0 p-2 z-10 text-accent bg-secondary hover:bg-highlight hover:text-primary border-accent border-b-2 border-r-2"
					onClick={() => navigator('/dataset')}
				>
					Return
				</button>
			</Root.In>
		</>
	);
};

export default SkullTechniqueID;
