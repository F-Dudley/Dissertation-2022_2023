import { type FC, type ReactNode, useRef, Suspense } from 'react';
import { LoaderProto, useLoader } from '@react-three/fiber';
import { Points } from '@react-three/drei';
import { PLYLoader } from 'three/examples/jsm/loaders/PLYLoader.js';

interface PCDViewerProps {
	dir: string;
	loader?: LoaderProto<undefined>;
	loading?: ReactNode;
}

const PCDViewer: FC<PCDViewerProps> = ({ dir, loader, loading = null }) => {
	const ref = useRef(null);
	const pcd = useLoader(loader ? loader : PLYLoader, dir);

	return (
		<Suspense fallback={loading}>
			<Points
				ref={ref}
				positions={pcd.attributes.position.array}
				colors={pcd.attributes.color.array}
				range={20}
			>
				<pointsMaterial size={0.0003} vertexColors />
			</Points>
		</Suspense>
	);
};

export default PCDViewer;
