import { Suspense, useMemo, useRef, useState } from 'react';
import { type BufferAttribute, SphereGeometry, Vector3, Mesh } from 'three';
import { Points } from '@react-three/drei';
import { ThreeElements, useFrame } from '@react-three/fiber';
import { DemoSphereLines } from '@/utils/three';

const MethodsPage = () => {
	const [registerClouds, setRegisterClouds] = useState<boolean>(true);
	const [showDistanceLines, setShowDistanceLines] = useState<boolean>(true);

	const smallSphereRef = useRef<Mesh>(null);
	const sphereRef = useRef<Mesh>(null);

	const smallerSphereGeometry = useMemo(
		() => new SphereGeometry(0.5, 15, 15),
		[],
	);
	const sphereGeometry = useMemo(() => new SphereGeometry(1, 15, 15), []);

	const calcLinePoints = useMemo(() => {
		const smallPoints = smallerSphereGeometry.attributes
			.position as BufferAttribute;
		const bigPoints = sphereGeometry.attributes.position as BufferAttribute;

		return DemoSphereLines(smallPoints, bigPoints);
	}, [smallerSphereGeometry, sphereGeometry]);

	useFrame(() => {
		if (smallSphereRef.current !== null) {
			smallSphereRef.current.position.lerp(
				registerClouds ? new Vector3(0, 0, 0) : new Vector3(2, 0, 0),
				0.1,
			);
		}
		if (sphereRef.current !== null) {
			sphereRef.current.position.lerp(
				registerClouds ? new Vector3(0, 0, 0) : new Vector3(-2.5, 0, 0),
				0.1,
			);
		}
	});

	return (
		<>
			<Suspense fallback={null}>
				<mesh ref={smallSphereRef} position={[2, 0, 0]}>
					<Points
						positions={
							smallerSphereGeometry.attributes.position.array
						}
					>
						<pointsMaterial size={0.01} color="green" />
					</Points>
				</mesh>
				<mesh ref={sphereRef} position={[-2, 0, 0]}>
					<Points
						positions={sphereGeometry.attributes.position.array}
					>
						<pointsMaterial size={0.01} color="red" />
					</Points>
				</mesh>
				{showDistanceLines && (
					<mesh>
						<lineSegments>
							<bufferGeometry>
								<bufferAttribute
									attach={'attributes-position'}
									args={[calcLinePoints, 3]}
								/>
							</bufferGeometry>
							<lineBasicMaterial color="blue" opacity={0.05} />
						</lineSegments>
					</mesh>
				)}
			</Suspense>
		</>
	);
};

export default MethodsPage;
