import {
	type FC,
	type ReactNode,
	useRef,
	Suspense,
	useMemo,
	forwardRef,
} from 'react';
import { LoaderProto, useLoader } from '@react-three/fiber';
import { Points, Float } from '@react-three/drei';
import { PLYLoader } from 'three/examples/jsm/loaders/PLYLoader.js';

interface PCDViewerProps {
	dir: string;
	loader?: LoaderProto<undefined>;
	loading?: ReactNode;
	pointScale?: number;
}

const PCDViewer: FC<PCDViewerProps> = forwardRef(
	({ dir, loader, loading = null, pointScale }, ref) => {
		const pcd = useMemo(
			() => useLoader(loader ? loader : PLYLoader, dir),
			[dir, loader],
		);

		return (
			<Suspense fallback={loading}>
				<Points
					ref={ref}
					positions={pcd.attributes.position.array}
					colors={pcd.attributes.color.array}
					range={20}
				>
					<pointsMaterial
						size={pointScale ? pointScale : 0.0003}
						vertexColors
					/>
				</Points>
			</Suspense>
		);
	},
);

export default PCDViewer;
