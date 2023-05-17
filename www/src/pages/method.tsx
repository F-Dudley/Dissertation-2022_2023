import { Suspense, useMemo, useRef, useState } from 'react';
import { type BufferAttribute, Vector3, Mesh } from 'three';
import { BBAnchor, Html, Points } from '@react-three/drei';
import { useFrame } from '@react-three/fiber';
import { DemoSphereLines, DemoSpherePoints } from '@/utils/Clouds';
import Root from '@/components/tunnels/Root';
import { useNavigate } from 'react-router';

enum MethodStates {
	Initial_State,
	Registered,
	Computed_Distance,
	Seperated,
}

const MaxMethodState = MethodStates.Seperated;

const MeetsState = (currState: number, target: MethodStates): boolean => {
	return currState >= target;
};

const MethodsPage = () => {
	const [currentStage, setMethodStage] = useState<number>(0);

	const smallSphereRef = useRef<Mesh>(null);
	const sphereRef = useRef<Mesh>(null);

	const smallSpherePos = useMemo<BufferAttribute>(
		() => DemoSpherePoints(0.75, 15, 15),
		[],
	);
	const largeSpherePos = useMemo<BufferAttribute>(
		() => DemoSpherePoints(1, 15, 15),
		[],
	);

	const LinePoints = useMemo(
		() => DemoSphereLines(smallSpherePos, largeSpherePos),
		[smallSpherePos, largeSpherePos],
	);

	const navigator = useNavigate();

	useFrame(() => {
		if (smallSphereRef.current !== null) {
			smallSphereRef.current.position.lerp(
				MeetsState(currentStage, MethodStates.Registered) &&
					!MeetsState(currentStage, MethodStates.Seperated)
					? new Vector3(0, 0, 0)
					: new Vector3(2, 0, 0),
				0.1,
			);
		}
		if (sphereRef.current !== null) {
			sphereRef.current.position.lerp(
				MeetsState(currentStage, MethodStates.Registered) &&
					!MeetsState(currentStage, MethodStates.Seperated)
					? new Vector3(0, 0, 0)
					: new Vector3(-2.5, 0, 0),
				0.1,
			);
		}
	});

	return (
		<>
			<Suspense fallback={null}>
				<mesh
					key="small-sphere-cloud"
					ref={smallSphereRef}
					position={[2, 0, 0]}
				>
					<Points positions={smallSpherePos.array as Float32Array}>
						<pointsMaterial size={0.03} color="green" />
					</Points>
					{MeetsState(currentStage, MethodStates.Initial_State) &&
						!MeetsState(
							currentStage,
							MethodStates.Computed_Distance,
						) && (
							<Html position={[0, -1.5, 0]} center>
								<div className="text-accent text-center select-none">
									Base Cloud
								</div>
							</Html>
						)}
				</mesh>
				<mesh
					key="large-sphere-cloud"
					ref={sphereRef}
					position={[-2, 0, 0]}
				>
					<Points positions={largeSpherePos.array as Float32Array}>
						<pointsMaterial size={0.03} color="red" />
					</Points>
					{MeetsState(currentStage, MethodStates.Initial_State) &&
						!MeetsState(
							currentStage,
							MethodStates.Computed_Distance,
						) && (
							<Html position={[0, 1.5, 0]} center>
								<div className="text-accent text-center select-none">
									Collected Cloud
								</div>
							</Html>
						)}
				</mesh>
				{MeetsState(currentStage, MethodStates.Computed_Distance) && (
					<mesh>
						<lineSegments>
							<bufferGeometry>
								<bufferAttribute
									attach={'attributes-position'}
									args={[LinePoints, 3]}
								/>
							</bufferGeometry>
							<lineBasicMaterial color="yellow" opacity={0.05} />
						</lineSegments>
						<Html position={[0, 1.5, 0]} center>
							<div className="text-accent text-center select-none">
								Point To Point Distance Calculation
							</div>
						</Html>
					</mesh>
				)}
			</Suspense>
			<Root.In>
				<div className="absolute flex flex-row justify-center p-2 w-full bottom-0  z-10 gap-5 bg-secondary border-accent border-t-2">
					<button
						className="bg-primary hover:bg-highlight hover:text-primary px-4"
						onClick={() =>
							setMethodStage((currVal) => {
								const newVal = currVal - 1;
								if (newVal < 0) {
									return MaxMethodState;
								}
								return newVal;
							})
						}
					>
						{'<<'}
					</button>
					<div className="bg-tertiary px-4">
						<span className="text-highlight">
							{MethodStates[currentStage].replace('_', ' ')}
						</span>
					</div>
					<button
						className="bg-primary hover:bg-highlight hover:text-primary px-4"
						onClick={() =>
							setMethodStage(
								(currVal) =>
									(currVal + 1) % (MaxMethodState + 1),
							)
						}
					>
						{'>>'}
					</button>
				</div>
				<button
					className="absolute top-0 p-2 z-10 text-accent bg-secondary hover:bg-highlight hover:text-primary border-accent border-b-2 border-r-2"
					onClick={() => navigator('/')}
				>
					Return
				</button>
			</Root.In>
		</>
	);
};

export default MethodsPage;
