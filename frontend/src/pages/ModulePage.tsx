import { Card } from '../components/ui/Card'
import { PageHeader } from '../components/ui/PageHeader'
import { ApiPendingState } from '../components/ui/StateViews'
import type { NavItem } from '../routes/navigation'

/**
 * Temporary shell for modules whose backend API is not ready.
 * It will be replaced module by module in later stages.
 */
export function ModulePage({ item }: { item: NavItem }) {
  return (
    <>
      <PageHeader title={item.label} description={item.description} />
      <Card>
        <ApiPendingState dependency={item.dependency} />
      </Card>
    </>
  )
}
