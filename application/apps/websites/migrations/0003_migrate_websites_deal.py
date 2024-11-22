# Generated by Django 5.1 on 2024-11-02 19:54

from django.db import migrations
from apps.migration.utils import fetch_data_from_mysql


def create_type_deals_func(apps, _schema_editor):
    TypeDeal = apps.get_model("websites", "TypeDeal")
    TypeDeal.objects.bulk_create(
        [
            TypeDeal(name="Affiliation"),
            TypeDeal(name="Direct payment"),
            TypeDeal(name="Link exchange"),
        ]
    )


def delete_type_deals_func(apps, _schema_editor):
    TypeDeal = apps.get_model("websites", "TypeDeal")
    TypeDeal.objects.filter(
        name__in=["Affiliation", "Direct payment", "Link exchange"]
    ).delete()


def create_payment_methods_func(apps, _schema_editor):
    PaymentMethod = apps.get_model("websites", "PaymentMethod")
    PaymentMethod.objects.bulk_create(
        [
            PaymentMethod(name="Paypal"),
            PaymentMethod(name="Bank transfer"),
            PaymentMethod(name="Crypto"),
        ]
    )


def delete_payment_methods_func(apps, _schema_editor):
    PaymentMethod = apps.get_model("websites", "PaymentMethod")
    PaymentMethod.objects.filter(
        name__in=["Paypal", "Bank transfer", "Crypto"]
    ).delete()


def create_deals_func(apps, _schema_editor):
    Deal = apps.get_model("websites", "Deal")
    TypeDeal = apps.get_model("websites", "TypeDeal")
    PaymentMethod = apps.get_model("websites", "PaymentMethod")
    deals = fetch_data_from_mysql("porn_deal")
    for deal in deals:
        current_deal = Deal.objects.create(
            id=deal.id,
            contact=deal.contact,
            status=deal.status,
            program=deal.program,
            start_date=deal.startdate,
            end_date=deal.enddate,
            amount_paid=deal.amount_paid,
            amount_available=deal.amount_available,
            payment_method=PaymentMethod.objects.get(name=deal.payment_method),
            potential=deal.potential,
            comment=deal.comment,
        )
        for type_d in [item.strip() for item in deal.type.split("+")]:
            current_deal.type.add(TypeDeal.objects.get(name=type_d))


def delete_deals_func(apps, _schema_editor):
    Deal = apps.get_model("websites", "Deal")
    deals = fetch_data_from_mysql("porn_deal")
    Deal.objects.filter(id__in=[r.id for r in deals]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("websites", "0002_migrate_websites_category_data"),
    ]

    operations = [
        migrations.RunPython(
            create_type_deals_func, delete_type_deals_func, atomic=True
        ),
        migrations.RunPython(
            create_payment_methods_func, delete_payment_methods_func, atomic=True
        ),
        migrations.RunPython(create_deals_func, delete_deals_func, atomic=True),
    ]
