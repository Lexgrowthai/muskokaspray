import { generatePageMetadata } from "@/lib/metadata";
import { serviceSchema, SITE_URL } from "@/lib/schema";
import SchemaScript from "@/components/schema/SchemaScript";
import AiReceptionistsClient from "./AiReceptionistsClient";

const NAME = "AI Receptionist For Law Firms";
const DESCRIPTION =
  "A 24/7 AI receptionist for law firms that answers every call, qualifies every lead, books consultations directly into your calendar, and escalates urgent matters — with Clio, MyCase, and CRM integration.";

export const metadata = generatePageMetadata({
  title: NAME,
  slug: "services/ai-receptionists",
  description: DESCRIPTION,
});

export default function AiReceptionistsPage() {
  return (
    <>
      <SchemaScript
        schema={serviceSchema(
          NAME,
          DESCRIPTION,
          `${SITE_URL}/services/ai-receptionists`
        )}
      />
      <AiReceptionistsClient />
    </>
  );
}
