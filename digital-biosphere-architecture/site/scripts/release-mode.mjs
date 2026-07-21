const MODES = new Set(["candidate", "formal"]);

function invariant(condition, message) {
  if (!condition) throw new Error(message);
}

function isHttpsUrl(value) {
  if (typeof value !== "string") return false;
  try {
    return new URL(value).protocol === "https:";
  } catch {
    return false;
  }
}

function requireValue(environment, name) {
  const value = environment[name]?.trim();
  invariant(value, `${name} is required for a formal release export`);
  return value;
}

export function resolveReleaseContext(environment, resources) {
  const mode = environment.RELEASE_MODE?.trim() || "candidate";
  invariant(MODES.has(mode), `RELEASE_MODE must be one of: ${[...MODES].join(", ")}`);

  const { status, agentIndex, agentCustomerPackage, dbosPackage } = resources;

  if (mode === "candidate") {
    invariant(status.release_claim === false, "candidate export requires status.release_claim=false");
    invariant(status.gates.DEVELOPER_PREVIEW_RELEASED === false, "candidate export requires DEVELOPER_PREVIEW_RELEASED=false");
    invariant(status.gates.DBOS_PUBLIC_SAFE_WHEEL_PUBLISHED === false, "candidate export requires DBOS_PUBLIC_SAFE_WHEEL_PUBLISHED=false");
    invariant(status.gates.DQ_016_DBOS_DISTRIBUTION_DECIDED === false, "candidate export requires DQ_016_DBOS_DISTRIBUTION_DECIDED=false");
    invariant(agentIndex.released === false, "candidate export requires agent-index released=false");
    invariant(agentCustomerPackage.released === false, "candidate export requires agent-customer package released=false");
    invariant(dbosPackage.release_authorized === false, "candidate export requires DBOS package release_authorized=false");
    invariant(dbosPackage.status === "VALIDATED_NOT_PUBLISHED", "candidate export requires DBOS package status VALIDATED_NOT_PUBLISHED");
    invariant(dbosPackage.public_download_url === null, "candidate export requires a null DBOS public download URL");

    return {
      mode,
      deploymentState: "candidate_not_released",
      developerPreviewReleased: false,
      releaseDecisionReference: null,
      releasedByRef: null,
      publicReleaseTag: null,
      dbosWheelUrl: null,
    };
  }

  const releaseDecisionReference = requireValue(environment, "RELEASE_DECISION_REF");
  const releasedByRef = requireValue(environment, "RELEASED_BY_REF");
  const publicReleaseTag = requireValue(environment, "PUBLIC_RELEASE_TAG");
  const dbosWheelUrl = requireValue(environment, "DBOS_WHEEL_URL");

  invariant(isHttpsUrl(dbosWheelUrl), "DBOS_WHEEL_URL must be an HTTPS URL");
  invariant(status.release_claim === true, "formal export requires status.release_claim=true");
  invariant(status.gates.DEVELOPER_PREVIEW_RELEASED === true, "formal export requires DEVELOPER_PREVIEW_RELEASED=true");
  invariant(status.gates.DBOS_PUBLIC_SAFE_WHEEL_PUBLISHED === true, "formal export requires DBOS_PUBLIC_SAFE_WHEEL_PUBLISHED=true");
  invariant(status.gates.DQ_016_DBOS_DISTRIBUTION_DECIDED === true, "formal export requires DQ_016_DBOS_DISTRIBUTION_DECIDED=true");
  invariant(agentIndex.released === true, "formal export requires agent-index released=true");
  invariant(agentCustomerPackage.released === true, "formal export requires agent-customer package released=true");
  invariant(dbosPackage.release_authorized === true, "formal export requires DBOS package release_authorized=true");
  invariant(dbosPackage.status === "PUBLISHED", "formal export requires DBOS package status PUBLISHED");
  invariant(dbosPackage.public_download_url === dbosWheelUrl, "DBOS_WHEEL_URL must match the DBOS package manifest");

  return {
    mode,
    deploymentState: "developer_preview_released",
    developerPreviewReleased: true,
    releaseDecisionReference,
    releasedByRef,
    publicReleaseTag,
    dbosWheelUrl,
  };
}

export function routeMarkers(mode) {
  if (mode === "formal") {
    return {
      zhHome: ["面向多智能体系统的可信基础设施", "正式发布：可信多智能体基础设施开发者预览版 v0.1"],
      enHome: ["Trust infrastructure for multi-agent systems", "Released: Trusted Multi-Agent Infrastructure Developer Preview v0.1"],
      zhStatus: ["可信多智能体基础设施开发者预览版 v0.1 已发布"],
      enStatus: ["Trusted Multi-Agent Infrastructure Developer Preview v0.1 is released"],
    };
  }

  return {
    zhHome: ["面向多智能体系统的可信基础设施", "不是正式发布"],
    enHome: ["Trust infrastructure for multi-agent systems", "not a release"],
    zhStatus: ["当前不是正式发布"],
    enStatus: ["This is not a release"],
  };
}
