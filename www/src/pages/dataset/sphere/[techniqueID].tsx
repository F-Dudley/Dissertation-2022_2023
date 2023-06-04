import { Suspense, useRef, useState, useMemo } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { Points } from '@react-three/drei';

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
	const [showDistMap, setShowDistMap] = useState<boolean>(false);

	const cloudDir = `/clouds/${techniqueID}/Sphere.ply`;
	const distMapCols = useMemo<Float32Array>(
		() => new Float32Array(DistMaps.get(techniqueID)),
		[techniqueID],
	);

	return (
		<>
			<Suspense fallback={<CanvasLoader />}>
				<PCDViewer
					ref={cloudRef}
					dir={cloudDir}
					loading={<CanvasLoader />}
					customColors={showDistMap ? distMapCols : undefined}
				/>
			</Suspense>
			<Root.In>
				<div className="absolute flex flex-row justify-center p-2 w-full bottom-0  z-10 gap-5 bg-secondary border-accent border-t-2">
					<input
						type="checkbox"
						checked={showDistMap}
						onChange={() => setShowDistMap((currVal) => !currVal)}
					/>
					<span className="text-accent">Show Distance Map</span>
				</div>
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

export default SphereTechniqueID;
